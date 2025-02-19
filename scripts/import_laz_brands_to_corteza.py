
import requests
import json

import logging
import time

# Lazada API details
LAZADA_API_URL = "http://127.0.0.1:8000/Product/GetBrandByPages"
PAGE_SIZE = 200  # Maximum allowed per request
JSON_FILE = "lazada_brands.json"

# Corteza API details
CORTEZA_API_URL = "https://corteza1.phatle.dev/api/compose/namespace/429540262432276481/module/429838396144222209/record/"
AUTH_TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6IjQyNjYzNDgwMzg0NzYyNjc1MyIsImV4cCI6MTczOTQ0MDM0NywiaWF0IjoxNzM5NDMzMTQ3LCJpc3MiOiJjb3J0ZXphcHJvamVjdC5vcmciLCJqdGkiOiJNVERLTkdRWU5aTVRZSkMyTUMwWk1US1hMVEdYTUdFVFlaRzVaVFJKTUdFV01KRkgiLCJyb2xlcyI6WyI0MjY2MzQ4MDM4NDUxMzYzODUiXSwic2NvcGUiOiJwcm9maWxlIGFwaSIsInN1YiI6IjQyNjYzNDgwMzg0Nzg4ODg5NyJ9.mq_7DbDWxX0_s1mrCXiFEhm-Jr3FPuwvLvaqcEx5lgxZymII7AAkg3sN_Up6ie_UojEFYyqKtNOiyns7XPYWqQ"
BATCH_SIZE = 2000  # Number of records per request

def fetch_brands():
    """Fetch all brands from Lazada and save to JSON file."""
    brands = []
    start_row = 0
    
    while True:
        params = {"startRow": start_row, "pageSize": PAGE_SIZE}
        response = requests.get(LAZADA_API_URL, params=params, headers={"Accept": "application/json"})
        
        if response.status_code != 200:
            logging.error(f"Failed to fetch brands at startRow {start_row}: {response.status_code}")
            break
        
        data = response.json()
        if not data.get("success"):
            logging.error(f"API error response at startRow {start_row}: {data}")
            break
        
        batch = data["data"].get("module", [])
        if not batch:
            break
        
        brands.extend(batch)
        logging.info(f"Fetched {len(batch)} brands from Lazada at startRow {start_row}.")
        
        start_row += PAGE_SIZE
        
        # Stop if all records are fetched
        if start_row >= data["data"]["total_record"]:
            break
        
        time.sleep(0.5)  # Prevent overwhelming the API
    
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(brands, f, indent=4)
    logging.info(f"Saved {len(brands)} brands to {JSON_FILE}.")

def import_to_corteza():
    """Import brands from JSON file into Corteza in batches."""
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            brands = json.load(f)
    except FileNotFoundError:
        logging.error(f"JSON file {JSON_FILE} not found.")
        return
    
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    for i in range(0, len(brands), BATCH_SIZE):
        batch = brands[i:i + BATCH_SIZE]
        records = [{
            "set": [{
                "values": [
                    {"name": "name", "value": brand["name"]},
                    {"name": "global_identifier", "value": brand["global_identifier"]},
                    {"name": "name_en", "value": brand["name_en"]},
                    {"name": "brand_id", "value": str(brand["brand_id"])}
                ]
            } for brand in batch ]
        }]
        
        response = requests.post(CORTEZA_API_URL, json={"records": records}, headers=headers)
        
        time.sleep(0.5)
        
        if response.status_code == 200:
            logging.info(f"Successfully imported batch {i // BATCH_SIZE + 1} with {len(batch)} brands.")
        else:
            logging.error(f"Failed to import batch {i // BATCH_SIZE + 1}: {response.status_code}, {response.text}")


# import_to_corteza()

def main():
  # Configure logging
    logging.basicConfig(
        filename='import_lazada_brands.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Starting Lazada brand fetch and import script.")
    fetch_brands()
    import_to_corteza()
    logging.info("Script execution completed.")

if __name__ == "__main__":
    main()