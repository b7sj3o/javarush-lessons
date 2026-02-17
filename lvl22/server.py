from fastapi import FastAPI
import asyncio
import uvicorn


app = FastAPI()

@app.get("/calculate")
async def calculate():
    await asyncio.sleep(2)
    return {
        "result": True
    }



uvicorn.run(app, host="0.0.0.0", port=8000)

