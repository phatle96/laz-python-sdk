import lazop
import os
import datetime as dt

url = os.getenv('LAZADA_URL')
appkey = os.getenv('LAZADA_APP_KEY')
appSecret = os.getenv('LAZADA_APP_SECRET')
access_token = os.getenv('LAZADA_ACCESS_TOKEN')

timeNow = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0800')

client = lazop.LazopClient(url, appkey ,appSecret)
request = lazop.LazopRequest('/products/get','GET')
# request.add_api_param('filter', 'live')
# request.add_api_param('update_before', '2018-01-01T00:00:00+0800')
request.add_api_param('create_before', timeNow)
# request.add_api_param('create_after', '2010-01-01T00:00:00+0800')
# request.add_api_param('update_after', '2010-01-01T00:00:00+0800')
# request.add_api_param('limit', '1')
# request.add_api_param('options', '1')
# request.add_api_param('sku_seller_list', ' [\"39817:01:01\", \"Apple 6S Black\"]')
response = client.execute(request, access_token)
print(response.type)
print(response.body)