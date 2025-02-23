from fastapi import FastAPI, UploadFile, File, HTTPException, Body
import requests
import uvicorn
import os
import whisper
# Import your local feature functions from VS Code files
from Main_points import extract_main_points
from Meeting_report import generate_meeting_report
from summariser import summarise_transcript
# from todo_list import get_todo_list, add_todo, delete_todo

app = FastAPI()

# -----------------------------------------------------------------------------
# 2. Extract Main Points Endpoint
# -----------------------------------------------------------------------------
@app.post("/extract-main-points/")
async def extract_main_points_endpoint(payload: dict = Body(...)):
    """
    Accepts a JSON body with a 'text' field, extracts main points using the
    function from mainpoints.py, and returns them.
    """
    text = payload.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    points = extract_main_points(text)
    return {"main_points": points}

# -----------------------------------------------------------------------------
# 3. Generate Meeting Report Endpoint
# -----------------------------------------------------------------------------
@app.post("/generate-report/")
async def generate_meeting_report_endpoint(payload: dict = Body(...)):
    """
    Accepts a JSON body with a 'text' field, generates a meeting report using
    meetingreports.py, and returns the report.
    """
    text = payload.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    report = generate_meeting_report(text)
    return {"meeting_report": report}

# -----------------------------------------------------------------------------
# 4. Summarization Endpoint
# -----------------------------------------------------------------------------
@app.post("/summarize/")
async def summarize_text_endpoint(payload: dict = Body(...)):
    """
    Accepts a JSON body with a 'text' field, summarizes the text using
    summariser.py, and returns the summary.
    """
    text = payload.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    summary = summarise_transcript(text)
    return {"summary": summary}

# -----------------------------------------------------------------------------
# 5. Todo List Endpoints
# -----------------------------------------------------------------------------
# @app.get("/todo/")
# async def get_todo_endpoint():
#     """
#     Returns the current todo list.
#     """
#     todos = get_todo_list()
#     return {"todo_list": todos}

# @app.post("/todo/")
# async def add_todo_endpoint(payload: dict = Body(...)):
#     """
#     Accepts a JSON body with a 'task' field and adds it to the todo list.
#     """
#     task = payload.get("task", "")
#     if not task:
#         raise HTTPException(status_code=400, detail="Task is required")
    
#     add_todo(task)
#     return {"message": "Task added successfully"}

# @app.delete("/todo/")
# async def delete_todo_endpoint(payload: dict = Body(...)):
#     """
#     Accepts a JSON body with a 'task' field and removes it from the todo list.
#     """
#     task = payload.get("task", "")
#     if not task:
#         raise HTTPException(status_code=400, detail="Task is required")
    
#     delete_todo(task)
#     return {"message": "Task deleted successfully"}

# -----------------------------------------------------------------------------
# Run the FastAPI application (for VS Code or production server)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
