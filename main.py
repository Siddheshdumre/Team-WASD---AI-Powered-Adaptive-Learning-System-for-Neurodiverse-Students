from fastapi import FastAPI
from routes import adhd, dyslexia, learning_speed
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Neurodiverse Learning Test API")

app.include_router(adhd.router, prefix="/adhd", tags=["ADHD Test"])
app.include_router(dyslexia.router, prefix="/dyslexia", tags=["Dyslexia Test"])
app.include_router(learning_speed.router, prefix="/learning_speed", tags=["Learning Speed Test"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the Neurodiverse Learning API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
