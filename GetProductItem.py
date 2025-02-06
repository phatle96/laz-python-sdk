import lazop
import os

url = os.getenv('LAZADA_URL')
appkey = os.getenv('LAZADA_APP_KEY')
appSecret = os.getenv('LAZADA_APP_SECRET')
access_token = os.getenv('LAZADA_ACCESS_TOKEN')

seller_sku = 'Cross-20'
item_id = '4496725150'

client = lazop.LazopClient(url, appkey ,appSecret)
request = lazop.LazopRequest('/product/item/get','GET')
request.add_api_param('item_id', item_id)
# request.add_api_param('seller_sku', seller_sku)
response = client.execute(request, access_token)
print(response.type)
print(response.body)