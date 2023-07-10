from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

task_list = []

class Task(BaseModel):
  id:int | None = None
  name: str
  date: datetime
  description: str | None = None

app = FastAPI()

@app.get('/')
def root():
  return {
    'message': 'Hello World'
  }

@app.post('/tasks')
async def create_task(task: Task):
  task.id = len(task_list)+1
  task_list.append(task)
  return task

@app.put('/tasks/{id}')
async def update_task(id:int,task:Task):
  task.id = id
  task_list[id-1] = task
  return task

@app.get('/tasks/all')
async def view_all_task():
  return task_list

@app.get('/tasks/{id}')
async def view_task(id:int):
  return task_list[id-1]
