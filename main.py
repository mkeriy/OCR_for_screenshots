from typing import List
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse,ORJSONResponse
from fastapi.templating import Jinja2Templates
from ocr import det_and_rec, draw_detected

app = FastAPI()

templates = Jinja2Templates("templates")

@app.post("/output", response_class=ORJSONResponse)
async def img_processing(
    files: List[bytes] = File(description="Multiple files as bytes")
):
    result, res = det_and_rec(files[0])
    # draw_detected(files[0], res)
    return  ORJSONResponse(result)

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request})



