import requests
import json
import logging
from datetime import datetime
import time

from lazservices import Product as LazProduct

# Configure logging
logging.basicConfig(
    filename=f'lazada_products_import_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_lazada_products(limit=50, offset=0):
    try:
        # headers = {
        #     'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        #     'accept': 'application/json',
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        # }
        # params = {'limit': limit, 'offset': offset}
        # response = requests.get(LAZADA_API_URL, headers=headers, params=params)
        # response.raise_for_status()
        # return response.json()
        
        response = LazProduct.get_products(limit, offset)
        return response
    except Exception as e:
        logging.error(f'Error fetching Lazada products: {str(e)}')
        return None

def prepare_product_basic_payload(product):
    images = product.get('images', [])
    images.extend([''] * (8 - len(images)))  # Pad with empty strings up to 8 images
    
    return {
        "values": [
            {"name": "productId", "value": str(product['item_id'])},
            {"name": "productName", "value": product['attributes'].get('name', '')},
            {"name": "productNameMY", "value": product['attributes'].get('name_ms', '')},
            {"name": "status", "value": product['status']},
            *[{"name": f"image{i+1}", "value": img} for i, img in enumerate(images)],
            {"name": "warranty", "value": product['attributes'].get('warranty', '')},
            {"name": "warrantyType", "value": product['attributes'].get('warranty_type', '')},
            {"name": "warrantyPolicy", "value": product['attributes'].get('product_warranty', '')},
            {"name": "mainDescription", "value": product['attributes'].get('description', '')},
            {"name": "shortDescription", "value": product['attributes'].get('short_description', '')}
        ]
    }

def prepare_sku_payload(product, sku):
    sku_images = sku.get('Images', [])
    sku_images.extend([''] * (8 - len(sku_images)))  # Pad with empty strings up to 8 images
    
    return {
        "values": [
            {"name": "productId", "value": str(product['item_id'])},
            {"name": "productName", "value": product['attributes'].get('name', '')},
            {"name": "skuId", "value": str(sku['SkuId'])},
            {"name": "sellerSku", "value": sku.get('SellerSku', '')},
            {"name": "shopSku", "value": sku.get('ShopSku', '')},
            {"name": "productUrl", "value": sku.get('Url', '')},
            {"name": "status", "value": sku.get('Status', '')},
            {"name": "price", "value": str(sku.get('price', ''))},
            {"name": "specialPrice", "value": str(sku.get('special_price', ''))},
            {"name": "specialFromDate", "value": sku.get('special_from_time', '')},
            {"name": "specialToDate", "value": sku.get('special_to_time', '')},
            {"name": "specialTimeFormat", "value": sku.get('special_time_format', '')},
            {"name": "quantity", "value": str(sku.get('quantity', ''))},
            {"name": "packageWidth", "value": sku.get('package_width', '')},
            {"name": "packageHeight", "value": sku.get('package_height', '')},
            {"name": "packageLength", "value": sku.get('package_length', '')},
            {"name": "packageWeight", "value": sku.get('package_weight', '')},
            {"name": "packageContent", "value": sku.get('package_content', '')},
            {"name": "variation", "value": json.dumps(sku.get('saleProp', {}))},
            *[{"name": f"skuImage{i+1}", "value": img} for i, img in enumerate(sku_images)]
        ]
    }

def import_to_corteza(url, records, token):
    try:
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        payload = {"records": [{"set": records}]}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return True
    except Exception as e:
        logging.error(f'Error importing to Corteza: {str(e)}')
        return False

def run(cortezaBaseUrl: str, namespaceID, token: str, productModuleId: str, skuModuleId: str):
    
    # Configuration
    LAZADA_API_URL = 'http://127.0.0.1:8000/Product/GetProducts'
    CORTEZA_BASE_URL = f'{cortezaBaseUrl}/api/compose/namespace/{namespaceID}'
    PRODUCT_MODULE_URL = f'{CORTEZA_BASE_URL}/module/{productModuleId}/record/'
    SKU_MODULE_URL = f'{CORTEZA_BASE_URL}/module/{skuModuleId}/record/'
    BATCH_SIZE = 50
    
    # Replace with your actual token
    corteza_token = f'{token}'
    offset = 0
    total_processed = 0
    
    try:
        while True:
            logging.info(f'Fetching products with offset {offset}')
            response = get_lazada_products(BATCH_SIZE, offset)
            
            if not response or 'data' not in response:
                break
                
            products = response['data']['products']
            if not products:
                break
                
            # Save raw data to JSON file
            with open(f'lazada_products_{offset}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json', 'w') as f:
                json.dump(products, f, indent=2)
            
            # Process basic product data
            basic_records = [prepare_product_basic_payload(product) for product in products]
            if import_to_corteza(PRODUCT_MODULE_URL, basic_records, corteza_token):
                logging.info(f'Successfully imported {len(basic_records)} basic product records')
            
            # Process SKU data
            for product in products:
                sku_records = [prepare_sku_payload(product, sku) for sku in product.get('skus', [])]
                if sku_records and import_to_corteza(SKU_MODULE_URL, sku_records, corteza_token):
                    logging.info(f'Successfully imported {len(sku_records)} SKU records for product {product["item_id"]}')
            
            total_processed += len(products)
            logging.info(f'Total products processed: {total_processed}')
            
            offset += BATCH_SIZE
            time.sleep(1)  # Rate limiting
            
    except Exception as e:
        logging.error(f'Main process error: {str(e)}')