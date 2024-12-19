from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Directory for storing video files
UPLOAD_DIRECTORY = "/Users/kamakshi/py/uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# In-memory storage for video metadata
video_metadata_store = {}

@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    # Save the file to the local directory
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Save file metadata in memory
    video_metadata_store[file.filename] = {
        "file_path": file_path,
        "status": "uploaded successfully",
    }

    return {"filename": file.filename, "status": "uploaded successfully"}

@app.get("/get-video/{filename}")
async def get_video(filename: str):
    # Retrieve file metadata from the in-memory store
    video_metadata = video_metadata_store.get(filename)

    if video_metadata:
        video_path = video_metadata["file_path"]
        if os.path.exists(video_path):
            return FileResponse(video_path)
        return {"error": "File exists in metadata but not on disk"}

    return {"error": "File not found"}
