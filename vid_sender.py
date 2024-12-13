from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["video_storage"]  # Database name
videos_collection = db["videos"]  # Collection name

@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    upload_directory = "/Users/kamakshi/py/uploads/"
    os.makedirs(upload_directory, exist_ok=True)
    file_path = os.path.join(upload_directory, file.filename)

    # Save the file to the local directory
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Save file metadata to MongoDB
    video_metadata = {
        "filename": file.filename,
        "file_path": file_path,
        "status": "uploaded successfully"
    }
    videos_collection.insert_one(video_metadata)

    return {"filename": file.filename, "status": "uploaded successfully"}

@app.get("/get-video/{filename}")
async def get_video(filename: str):
    # Retrieve file metadata from MongoDB
    video_metadata = videos_collection.find_one({"filename": filename})

    if video_metadata:
        video_path = video_metadata["file_path"]
        if os.path.exists(video_path):
            return FileResponse(video_path)
        return {"error": "File exists in the database but not on disk"}

    return {"error": "File not found in the database"}
