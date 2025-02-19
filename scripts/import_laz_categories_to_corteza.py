import requests
import json
import logging

# Load the Lazada category tree from JSON file
def load_lazada_data(filename):
    logging.info(f"Loading data from {filename}")
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)["data"]

# Recursive function to flatten category tree
def process_categories(categories, path=""):
    logging.info("Processing category tree")
    result = []
    for category in categories:
        current_path = f"{path}/{category['name']}" if path else category['name']
        entry = {
            "var": category["var"],
            "name": category["name"],
            "leaf": category["leaf"],
            "category_id": category["category_id"],
            "path": current_path
        }
        result.append(entry)
        
        if not category["leaf"] and "children" in category:
            result.extend(process_categories(category["children"], current_path))
    
    return result

# Save processed data to JSON file
def save_transformed_data(data, filename):
    logging.info(f"Saving transformed data to {filename}")
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Send data to Corteza API in batches of 500 records per request
def send_to_corteza(api_url, token, data, batch_size=500):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        logging.info(f"Sending batch {i // batch_size + 1} with {len(batch)} records")
        payload = {
            "records": [{"set": [{"values": [
                {"name": "var", "value": str(entry["var"])},
                {"name": "name", "value": entry["name"]},
                {"name": "leaf", "value": str(entry["leaf"])},
                {"name": "category_id", "value": str(entry["category_id"])},
                {"name": "path", "value": entry["path"]}
            ]} for entry in batch]}]
        }
        
        response = requests.post(api_url, headers=headers, json=payload)
        logging.info(f"Batch {i // batch_size + 1} response: {response.status_code}")

# Main execution
if __name__ == "__main__":
    INPUT_FILE = "laz-category-tree.json"
    OUTPUT_FILE = "transformed_categories.json"
    API_URL = "https://corteza1.phatle.dev/api/compose/namespace/429540262432276481/module/429842612996800513/record/"
    API_TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6IjQyNjYzNDgwMzg0NzYyNjc1MyIsImV4cCI6MTczOTQ0MTQ4OSwiaWF0IjoxNzM5NDM0Mjg5LCJpc3MiOiJjb3J0ZXphcHJvamVjdC5vcmciLCJqdGkiOiJNWkkxTlRETFpNTVRZV1EyTkkwWk1aS1pMV0ZMWkpNVE5aVkpOWkNaTlRKS1pXVkwiLCJyb2xlcyI6WyI0MjY2MzQ4MDM4NDUxMzYzODUiXSwic2NvcGUiOiJwcm9maWxlIGFwaSIsInN1YiI6IjQyNjYzNDgwMzg0Nzg4ODg5NyJ9.LguvINe9o-WNq0clXXplSyUmkCCqjzONKRASzbk7RyyDGMedDCD8Krzo34WAxnCVLVUFhtdShFd8O2A__YxtTw"  # Replace with your actual API token
    
    # Configure logging
    logging.basicConfig(filename='import_lazada_categories.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    category_data = load_lazada_data(INPUT_FILE)
    transformed_data = process_categories(category_data)
    save_transformed_data(transformed_data, OUTPUT_FILE)
    
    send_to_corteza(API_URL, API_TOKEN, transformed_data, batch_size=500)
