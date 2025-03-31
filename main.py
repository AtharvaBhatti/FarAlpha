from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"status": "Online"}

@app.get("/sayHello")
async def say_hello():
    return {"message": "Hello User"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
