import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Agent is running!"}

if __name__ == "__main__":
    import uvicorn
    # Render بيحدد الـ PORT أوتوماتيك في الـ Environment
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)