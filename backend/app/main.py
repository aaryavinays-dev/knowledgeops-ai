from fastapi import FastAPI

app = FastAPI(
    title="KnowledgeOps AI Backend",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "KnowledgeOps AI Backend",
        "version": "0.1.0",
        "environment": "development"
    }