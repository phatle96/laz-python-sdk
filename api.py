from fastapi import FastAPI
from lazservices import Product as LazProduct
from lazmodels import CreateProductRequestModel
from scripts import create_lazada_product_basic_module as product_basic_module
from scripts import create_lazada_product_sku_module as product_sku_module
from scripts import import_laz_products_to_corteza as import_laz_products

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

@app.post("/Product/UpdateSkuPrice")
async def update_sku_price(sku_id: str, price: str):
    return LazProduct.update_sku_price(sku_id, price)

@app.post("/Corteza/Module/LazadaProductBasic/Create")
async def create_lazada_product_basic(cortezaBaseUrl: str, connectionID: str, token: str, namespaceID: str, moduleName: str, moduleHandle: str):
    return product_basic_module.create_lazada_product_basic_module(cortezaBaseUrl, connectionID, token, namespaceID, moduleName, moduleHandle)

@app.post("/Corteza/Module/LazadaProductSku/Create")
async def create_lazada_product_sku(cortezaBaseUrl: str, connectionID: str, token: str, namespaceID: str, moduleName: str, moduleHandle: str):
    return product_sku_module.create_lazada_product_sku_module(cortezaBaseUrl, connectionID, token, namespaceID, moduleName, moduleHandle)

@app.post("/Corteza/Product/Import")
async def import_laz_products_to_corteza(cortezaBaseUrl: str, namespaceID, token: str, productModuleId: str, skuModuleId: str):
    return import_laz_products.run(cortezaBaseUrl, namespaceID, token, productModuleId, skuModuleId)