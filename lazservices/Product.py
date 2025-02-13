import lazop
import os
import datetime as dt
import json

url = os.getenv('LAZADA_URL')
appkey = os.getenv('LAZADA_APP_KEY')
appSecret = os.getenv('LAZADA_APP_SECRET')
access_token = os.getenv('LAZADA_ACCESS_TOKEN')

client = lazop.LazopClient(url, appkey ,appSecret)

def get_products(limit: int = 50, offset: int = 0):
    
    timeNow = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0800')

    request = lazop.LazopRequest('/products/get','GET')
    
    request.add_api_param('limit', json.dumps(limit))
    request.add_api_param('create_before', timeNow)
    request.add_api_param('offset', json.dumps(offset))
    # request.add_api_param('filter', 'live')
    # request.add_api_param('update_before', '2018-01-01T00:00:00+0800')
    # request.add_api_param('create_after', '2010-01-01T00:00:00+0800')
    # request.add_api_param('update_after', '2010-01-01T00:00:00+0800')
    # request.add_api_param('options', '1')
    # request.add_api_param('sku_seller_list', ' [\"39817:01:01\", \"Apple 6S Black\"]')
    
    response = client.execute(request, access_token)
    return response.body

def get_product_item(item_id: int):
    
    request = lazop.LazopRequest('/product/item/get','GET')
    request.add_api_param('item_id', json.dumps(item_id))
    response = client.execute(request, access_token)
    
    return response.body


def create_product(data):
    
    request = lazop.LazopRequest('/product/create', 'POST')
    request.add_api_param('payload', data)
    response = client.execute(request, json.dumps(access_token))
    
    return response.body

def get_category_tree():
    
    request = lazop.LazopRequest('/category/tree/get','GET')
    request.add_api_param('language_code', 'en_US')
    response = client.execute(request)
    
    return response.body

def get_category_suggestion(product_name: str):
    
    request = lazop.LazopRequest('/product/category/suggestion/get','GET')
    request.add_api_param('product_name', json.dumps(product_name))
    response = client.execute(request, access_token)
    
    return response.body

def get_category_attributes(category_id: int):
    
    request = lazop.LazopRequest('/category/attributes/get','GET')
    request.add_api_param('primary_category_id', json.dumps(category_id))
    request.add_api_param('language_code', 'en_US')
    response = client.execute(request)
    
    return response.body

def migrate_image(image_url: str):
    
    payload = '<?xml version=\"1.0\" encoding=\"UTF-8\" ?> <Request>     <Image>         <Url>'+image_url+'</Url>     </Image> </Request>'
    
    request = lazop.LazopRequest('/image/migrate')
    request.add_api_param('payload', payload)
    response = client.execute(request, access_token)
    
    return response.body

def get_category_tree():
    
    request = lazop.LazopRequest('/category/tree/get','GET')
    request.add_api_param('language_code', 'en_US')
    response = client.execute(request)
    
    return response.body

def get_brand_by_pages(startRow: int = 0, pageSize: int = 50):
    
    request = lazop.LazopRequest('/category/brands/query')
    request.add_api_param('startRow', json.dumps(startRow))
    request.add_api_param('pageSize', json.dumps(pageSize))
    response = client.execute(request)
    
    return response.body

def update_sku_price(sku_id: str, price: str):
    
    data = f'<?xml version=\"1.0\" encoding=\"UTF-8\" ?><Request><Product><Skus><Sku><SkuId>{sku_id}</SkuId><price>{price}</price></Sku></Skus></Product></Request>'
    
    request = lazop.LazopRequest('/product/update', 'POST')
    request.add_api_param('payload', data)
    response = client.execute(request, access_token)
    return response.body