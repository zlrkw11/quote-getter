from fastapi import FastAPI
from app.routers import quote

app = FastAPI(
    title="Quote Getter API",
    version="0.1.0"
)

app.include_router(quote.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

