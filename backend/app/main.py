from fastapi import FastAPI

app = FastAPI(
    title="Authenova API",
    description="AI-powered identity and document verification platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Authenova API is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }