from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health():
    return {"status": "ok"}


Instrumentator().instrument(app).expose(app)


