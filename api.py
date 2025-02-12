from fastapi import FastAPI
from lazservices import Product as LazProduct
from lazmodels import CreateProductRequestModel

app = FastAPI()

@app.get("/Product/GetCategoryTree")
def get_category_tree():
    return LazProduct.get_category_tree()

@app.get("/Product/GetBrandByPages")
def get_brand_by_pages(startRow: int = 0, pageSize: int = 50):
    return LazProduct.get_brand_by_pages(startRow, pageSize)

@app.get("/Product/GetProducts")
def get_products(limit: int = 50, offset: int = 0):
    return LazProduct.get_products(limit, offset)

@app.get("/Product/GetProductItem/{item_id}")
def get_product_item(item_id: int):
    return LazProduct.get_product_item(item_id)

@app.get("/Product/GetCategorySuggestions/{product_name}")
def get_category_suggestion(product_name: str):
    return LazProduct.get_category_suggestion(product_name)

@app.get("/Product/GetCategoryAttributes/{category_id}")
def get_category_attributes(category_id: int):
    return LazProduct.get_category_attributes(category_id)

@app.post("/Image/Migrate")
def migrate_image(data):
    return LazProduct.migrate_image(data)

@app.post("/Product/Create")
async def create_product(data: CreateProductRequestModel):
    return LazProduct.create_product(data)
