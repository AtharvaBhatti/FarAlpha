from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"status" : "Online"}

@app.get("/sayHello")
async def simple():
    return { "message" : "Hello User"}

if __name__ == "__main__":
    PORT = 80
    uvicorn.run(app, host="127.0.0.1", port=PORT)