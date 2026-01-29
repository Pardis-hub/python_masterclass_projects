from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    price: float

products = [
    Product(name="TV", price=1200),
    Product(name="Phone", price=800),
    Product(name="headphones", price=25),
]


@app.get("/products", response_model=List[Product])
def get_products(max_price: Optional[float] = Query(None)):
    if max_price is not None:
        return [p for p in products if p.price < max_price]
    return products


@app.post("/products", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product


@app.get("/products/{id}", response_model=Product)
def get_product(id: UUID):
    for p in products:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@app.put("/products/{id}", response_model=Product)
def update_product(id: UUID, updated_product: Product):
    for index, p in enumerate(products):
        if p.id == id:
            updated_product.id = id
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{id}")
def delete_product(id: UUID):
    for index, p in enumerate(products):
        if p.id == id:
            products.pop(index)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")