from paddleocr import PaddleOCR, draw_ocr
import json, io
from PIL import Image
import numpy as np
import json


def det_and_rec(img):

    ocr = PaddleOCR(lang='ru')
     # need to run only once to download and load model into memory
    img_array = np.array(Image.open(io.BytesIO(img)).convert('RGB')) 
   
    res = ocr.ocr(img_array, cls=False)

    result = {}
    
    for idx in range(len(res)):
        print(res[idx])
        for line in res[idx]:
            result[line[-1][0]] = line[0]
    
    
    return result, res

# # draw result
def draw_detected(img: bytes, res):
    res=res[0]
    img_array = np.array(Image.open(io.BytesIO(img)).convert('RGB')) 
    boxes = [line[0] for line in res]
    im_show = draw_ocr(img_array, boxes)
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')



