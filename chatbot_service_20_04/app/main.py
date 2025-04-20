from fastapi import FastAPI
from app.routes.chatbot import router as chatbot_router
from app.routes.ui import router as ui_router

# Création de l'application FastAPI
app = FastAPI()

# Inclure les routeurs
app.include_router(chatbot_router, prefix="/api", tags=["Chatbot"])
app.include_router(ui_router, tags=["UI"])