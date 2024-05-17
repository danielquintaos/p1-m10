from fastapi import APIRouter, HTTPException, status
from typing import List
from pydantic import BaseModel

router = APIRouter()


# Pydantic models
class pedido(BaseModel):
    id: str
    title: str
    description: str

class Create(BaseModel):
    title: str
    description: str

# Routes
@router.get("/", response_model=List[pedido])
async def list_pedidos():
    return pedidos

@router.post("/", response_model=pedido, status_code=status.HTTP_201_CREATED)
async def create_pedido(pedido: createPedido):
    new_pedido = {"id": str(len(pedidos) + 1), **pedido.dict()}
    pedidos.append(new_pedido)
    return new_pedido

@router.get("/{pedido_id}", response_model=pedido)
async def get_pedido(pedido_id: str):
    for pedido in pedidos:
        if pedido["id"] == pedido_id:
            return pedido
    raise HTTPException(status_code=404, detail="pedido not found")

@router.put("/{pedido_id}", response_model=pedido)
async def update_pedido(pedido_id: str, pedido: createPedido):
    for index, current_pedido in enumerate(pedidos):
        if current_pedido["id"] == pedido_id:
            updated_pedido = {**current_pedido, **pedido.dict()}
            pedidos[index] = updated_pedido
            return updated_pedido
    raise HTTPException(status_code=404, detail="pedido not found")

@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pedido(pedido_id: str):
    global pedidos
    for index, current_pedido in enumerate(pedidos):
        if current_pedido["id"] == pedido_id:
            pedidos.pop(index)
            return
    raise HTTPException(status_code=404, detail="pedido not found")
