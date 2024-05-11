from fastapi import FastAPI
from fastapi.responses import FileResponse
from calculate import router as calculate_router

app = FastAPI()
app.include_router(calculate_router)

@app.get('/')
def root_html():
    return FileResponse("public/index.html")

