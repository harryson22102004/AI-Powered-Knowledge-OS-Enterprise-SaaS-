from fastapi import FastAPI
from auth_service.routes import router as auth_router
from document_service.routes import router as doc_router

app = FastAPI(title="CortexFlow API")

app.include_router(auth_router, prefix="/auth")
app.include_router(doc_router, prefix="/documents")
