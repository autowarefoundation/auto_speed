#%%
# Comment above is for Jupyter execution in VSCode
#! /usr/bin/env python3
import torch
import onnx
from argparse import ArgumentParser
import sys
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT))
from Models.model_components.auto_speed.auto_speed_network import AutoSpeedNetwork

def main():

    # Argument parser for data root path and save path
    parser = ArgumentParser()

    parser.add_argument("-p", "--model_checkpoint_path", dest="model_checkpoint_path", required=True, \
                        help="path to pytorch checkpoint file to load model dict")

    parser.add_argument("-o", "--onnx_model_path", dest="onnx_model_path", required=True, \
                        help="path to converted ONNX model, must include output file name with .onnx extension")

    args = parser.parse_args()

    # Get input arguments
    model_checkpoint_path = args.model_checkpoint_path
    onnx_model_path = args.onnx_model_path

    # Device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using {device} for inference')


    # Instantiating Model and setting to evaluation mode

    model = AutoSpeedNetwork().build_model(version='n', num_classes=4)

    # Loading Pytorch checkpoint
    print('Loading Network')
    if(len(model_checkpoint_path) > 0):
            checkpoint = torch.load(model_checkpoint_path, weights_only=False, map_location=device)
            # Handle different checkpoint formats
            if isinstance(checkpoint, dict) and 'model' in checkpoint:
                # If checkpoint['model'] is a model object, extract its state_dict
                if hasattr(checkpoint['model'], 'state_dict'):
                    model.load_state_dict(checkpoint['model'].state_dict())
                else:
                    model.load_state_dict(checkpoint['model'])
            else:
                model.load_state_dict(checkpoint)
    else:
        raise ValueError('No path to checkpiont file provided in class initialization')
    model = model.to(device)
    model = model.eval()

    # Fake input data
    input_shape=(1, 3, 512, 1024)

    input_data = torch.randn(input_shape).to(device)
    input_data_prev = torch.randn(input_shape).to(device)

    # Test inference
    print('Testing inference')

    _ = model(input_data)

    # Export FP32 model to onnx
    print('Converting model to ONNX at FP32 and exporting')

    torch.onnx.export(model,                                          # model
                    input_data,                                       # model input
                    onnx_model_path,                                  # path
                    export_params=True,                               # store the trained parameter weights inside the model file
                    opset_version=18,                                 # the ONNX version to export the model to
                    do_constant_folding=True,                         # constant folding for optimization
                    input_names = ['input'],                          # input names
                    output_names = ['output'],                        # output names
                    dynamic_axes={'input' : {0 : 'batch_size'},       # variable length axes
                                    'output' : {0 : 'batch_size'}},
                    external_data=False)

    # Run checks on exported FP32 ONNX network
    ONNX_network = onnx.load(onnx_model_path)
    onnx.checker.check_model(ONNX_network)
    print('Checks passed - export complete')

if __name__ == '__main__':
  main()
# %%