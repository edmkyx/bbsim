from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to BBSim API. Backend and simulation logic is ready!"}