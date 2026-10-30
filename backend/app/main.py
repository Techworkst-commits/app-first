from fastapi import FastAPI

app = FastAPI(title="GNU Prototype API")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Docker & FastAPI running successfully"}
