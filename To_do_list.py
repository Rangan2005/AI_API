from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


def manage_todo_list(request):
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    os.environ['GROQ_API_KEY'] = api_key
    model = ChatGroq(model="llama-3.1-8b-instant")
    """
    This function handles to-do list management requests like adding, removing, or displaying tasks.
    """
    prompt = f"""
You are an AI assistant specialized in managing to-do lists. Given the current list of tasks and a set of modifications, update the list and output your answer in the following format exactly:

**Current To-Do List:**
[List the tasks that remain after modifications]

**Task Status:**
- For each task, output a line with the task in single quotes, a colon, and its status.
  - When a new task is added, mark it as 'Pending'.
  - When a task is removed, mark it as 'Removed'.
  - For tasks that remain unchanged, mark them as 'Pending'.

Ensure that your response reflects all modifications accurately.


    Request:
    {request}
    """
    result = model.invoke(prompt)
    return result.content
