from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}