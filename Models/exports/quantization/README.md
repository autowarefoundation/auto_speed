# Quantization Export

In order to quantize auto_speed model use the `auto_speed_qdq.py` script.

```
python3 auto_speed_qdq.py -q -d <DATASET PATH> -fp32onnx <FP32 ONNX MODEL PATH> -int8onnx <QUANTIZED INT8 OUTPUT MODEL PATH>
```
