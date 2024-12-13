from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    upload_directory = "/Users/kamakshi/py/uploads/"
    os.makedirs(upload_directory, exist_ok=True)  
    file_path = os.path.join(upload_directory, file.filename)

    
    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"filename": file.filename, "status": "uploaded successfully"}


@app.get("/get-video/{filename}")
async def get_video(filename: str):
    video_path = os.path.join("/Users/kamakshi/py/uploads/", filename)
    if os.path.exists(video_path):
        return FileResponse(video_path)
    return {"error": "File not found"}
