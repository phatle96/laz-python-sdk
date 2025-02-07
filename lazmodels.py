from pydantic import BaseModel

class ProductModel(BaseModel): object
    

class CreateProductRequestModel(BaseModel):
    Request: ProductModel

    
