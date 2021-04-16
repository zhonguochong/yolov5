'''
Description: 
version: 
Author: Guochong Zhong
Date: 2021-02-23 21:06:13
LastEditors: Guochong Zhong
LastEditTime: 2021-02-23 21:27:23
'''
# import onnx
import numpy as np
import torch


# onnx_model = onnx.load('runs/train/exp11/weights/best.onnx')
# onnx.checker.check_model(onnx_model)
x = torch.randn(1, 3, 640, 640, requires_grad=True)
import onnxruntime
ort_session = onnxruntime.InferenceSession("runs/train/exp11/weights/best.onnx")
def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()
# ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(x)}
# ort_outs = ort_session.run(None, ort_inputs)

# # compare ONNX Runtime and PyTorch results
# np.testing.assert_allclose(to_numpy(torch_out), ort_outs[0], rtol=1e-03, atol=1e-05)
# print("Exported model has been tested with ONNXRuntime, and the result looks good!")

from PIL import Image
import torchvision.transforms as transforms

img = Image.open('/home/zgc/proj/jp/images/val0121/141.jpg')
image = np.asarray(img ,dtype=np.float32)
image = np.transpose(image,(2,0,1))##input in CHW format

ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(x)}
ort_outs = ort_session.run(None, ort_inputs)
print(ort_outs)