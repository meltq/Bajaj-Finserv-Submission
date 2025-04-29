from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uvicorn
import os
import json

json_f = ""

with open("data.json", "r") as f:
    json_f = json.load(f)

app = FastAPI()

if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get-lab-tests")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    return JSONResponse(content=json_f[str(file.filename)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
