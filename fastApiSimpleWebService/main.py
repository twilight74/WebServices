from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()


@app.post("/home/")
async def home():
    response = JSONResponse({"message": "You are in Home Page "})
    response.headers['x-frame-options'] = "X"
    response.headers['x-content-type-options'] = "X"
    response.headers['referrer-policy'] = "X"
    response.headers['cross-origin-opener-policy'] = "X"
    response.headers['content-type'] = "application/json"
    return response

