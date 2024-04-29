from fastapi import APIRouter, status, HTTPException
from models import ProductModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
import tempfile
import json
from data import data

router=APIRouter(
    prefix="/products",
    tags=['products']
)

@router.post('/products', status_code=status.HTTP_201_CREATED)
async def create_item(item: ProductModel):
    new_product_id = max(data.keys(), default=0) + 1  
    new_product = {
        "id": new_product_id,
        "name": item.name,
        "price": item.price,
        "description": item.description
    }
    data[new_product_id] = new_product  
    return {"id": new_product_id}

@router.get('/products/{product_id}')
async def get_item_by_id(product_id: int):
    item = data.get(product_id)  
    if item:
        return jsonable_encoder(item)
    else:
        raise HTTPException(status_code=404, detail="Продукт не найден")


@router.get('/products_download')
async def list_all_items():
    with tempfile.NamedTemporaryFile(delete=False, mode='w+b') as tmp_file:
        json_data = json.dumps(list(data.values())).encode('utf-8')
        tmp_file.write(json_data)
    return FileResponse(tmp_file.name, media_type="application/json", filename="products.json")
