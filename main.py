from fastapi import FastAPI

app = FastAPI()

@app.get("/BUILD-APIs/index")
def index():
    return{"message" : "Connection Successful!"}