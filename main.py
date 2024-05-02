from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
def root_html():
    return FileResponse("public/index.html")