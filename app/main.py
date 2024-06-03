from fastapi import FastAPI
from fastapi.responses import FileResponse
from routes.calculate import calculate
from routes.todo import todo_router

app = FastAPI()

@app.get('/')
def root_html():
    return FileResponse("public/index.html")

app.include_router(calculate)
app.include_router(todo_router)