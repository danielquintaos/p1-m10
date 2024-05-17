from fastapi import FastAPI
from .routes.pedido_router import router as pedido_router

app = FastAPI(title="pedido API", version="1.0.0", description="An API to manage pedidos")

# Include routers from the routes module
app.include_router(pedido_router, prefix="/pedidos", tags=["pedidos"])

@app.get("/")
async def root():
    return {"message": "PROVA 1!"}
