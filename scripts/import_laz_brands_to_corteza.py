
import requests
import json

import logging
import time

def check_corteza_module(cortezaUrl, cortezaBearerToken, cortezaNamespace, cortezaModuleName):

  url = f"{cortezaUrl}/api/compose/namespace/{cortezaNamespace}/module/?query={cortezaModuleName}&limit=100&incTotal=true&sort=name+ASC"

  payload = {}
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Authorization': f"{cortezaBearerToken}",
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)
  
def create_corteza_module(cortezaUrl, cortezaBearerToken, cortezaNamespace, cortezaModuleName, cortezaModuleHandle):

  url = f"{cortezaUrl}/api/compose/namespace/{cortezaNamespace}/module/"

  payload = json.dumps({
    "name": f"{cortezaModuleName}",
    "handle": f"{cortezaModuleHandle}",
    "config": {
      "dal": {
        "connectionID": "426634803845070849",
        "ident": "",
        "systemFieldEncoding": {
          "id": None,
          "revision": None,
          "moduleID": None,
          "namespaceID": None,
          "ownedBy": None,
          "createdBy": None,
          "createdAt": None,
          "updatedBy": None,
          "updatedAt": None,
          "deletedBy": None,
          "deletedAt": None
        }
      },
      "privacy": {
        "sensitivityLevelID": "0",
        "usageDisclosure": ""
      },
      "discovery": {
        "public": {
          "result": [
            {
              "lang": "",
              "fields": []
            }
          ]
        },
        "private": {
          "result": [
            {
              "lang": "",
              "fields": []
            }
          ]
        },
        "protected": {
          "result": [
            {
              "lang": "",
              "fields": []
            }
          ]
        }
      },
      "recordRevisions": {
        "enabled": False,
        "ident": ""
      },
      "recordDeDup": {
        "rules": []
      }
    },
    "meta": {},
    "fields": [
      {
        "fieldID": "0",
        "name": "name",
        "kind": "String",
        "label": "Name",
        "defaultValue": [],
        "maxLength": 0,
        "isRequired": False,
        "isMulti": False,
        "isSystem": False,
        "isSortable": True,
        "isFilterable": True,
        "options": {
          "description": {
            "view": ""
          },
          "hint": {
            "view": ""
          },
          "multiLine": False,
          "useRichTextEditor": False,
          "multiDelimiter": "\n"
        },
        "expressions": {
          "sanitizers": [
            ""
          ],
          "validators": [],
          "disableDefaultValidators": False,
          "formatters": [],
          "disableDefaultFormatters": False
        },
        "config": {
          "dal": {
            "encodingStrategy": None
          },
          "privacy": {
            "sensitivityLevelID": "0",
            "usageDisclosure": ""
          },
          "recordRevisions": {
            "enabled": False
          }
        },
        "canUpdateRecordValue": False,
        "canReadRecordValue": False
      },
      {
        "fieldID": "0",
        "name": "global_identifier",
        "kind": "String",
        "label": "Global Identifier",
        "defaultValue": [],
        "maxLength": 0,
        "isRequired": False,
        "isMulti": False,
        "isSystem": False,
        "isSortable": True,
        "isFilterable": True,
        "options": {
          "description": {
            "view": ""
          },
          "hint": {
            "view": ""
          },
          "multiLine": False,
          "useRichTextEditor": False,
          "multiDelimiter": "\n"
        },
        "expressions": {},
        "config": {
          "dal": {
            "encodingStrategy": None
          },
          "privacy": {
            "sensitivityLevelID": "0",
            "usageDisclosure": ""
          },
          "recordRevisions": {
            "enabled": False
          }
        },
        "canUpdateRecordValue": False,
        "canReadRecordValue": False
      },
      {
        "fieldID": "0",
        "name": "name_en",
        "kind": "String",
        "label": "Name En",
        "defaultValue": [],
        "maxLength": 0,
        "isRequired": False,
        "isMulti": False,
        "isSystem": False,
        "isSortable": True,
        "isFilterable": True,
        "options": {
          "description": {
            "view": ""
          },
          "hint": {
            "view": ""
          },
          "multiLine": False,
          "useRichTextEditor": False,
          "multiDelimiter": "\n"
        },
        "expressions": {},
        "config": {
          "dal": {
            "encodingStrategy": None
          },
          "privacy": {
            "sensitivityLevelID": "0",
            "usageDisclosure": ""
          },
          "recordRevisions": {
            "enabled": False
          }
        },
        "canUpdateRecordValue": False,
        "canReadRecordValue": False
      },
      {
        "fieldID": "0",
        "name": "brand_id",
        "kind": "String",
        "label": "Brand Id",
        "defaultValue": [],
        "maxLength": 0,
        "isRequired": False,
        "isMulti": False,
        "isSystem": False,
        "isSortable": True,
        "isFilterable": True,
        "options": {
          "description": {
            "view": ""
          },
          "hint": {
            "view": ""
          },
          "multiLine": False,
          "useRichTextEditor": False,
          "multiDelimiter": "\n"
        },
        "expressions": {},
        "config": {
          "dal": {
            "encodingStrategy": None
          },
          "privacy": {
            "sensitivityLevelID": "0",
            "usageDisclosure": ""
          },
          "recordRevisions": {
            "enabled": False
          }
        },
        "canUpdateRecordValue": False,
        "canReadRecordValue": False
      }
    ],
    "labels": {}
  })
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'Content-Type': 'application/json',
    'Authorization': f"{cortezaBearerToken}",
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(payload)
  print(response.text)




# Configure logging
logging.basicConfig(
    filename='import_lazada_brands.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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


import_to_corteza()

# def main():
#     logging.info("Starting Lazada brand fetch and import script.")
#     fetch_brands()
#     import_to_corteza()
#     logging.info("Script execution completed.")

# if __name__ == "__main__":
#     main()



# check_corteza_module("https://corteza1.phatle.dev",
#                      "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6IjQyNjYzNDgwMzg0NzYyNjc1MyIsImV4cCI6MTczOTQyOTg5OSwiaWF0IjoxNzM5NDIyNjk5LCJpc3MiOiJjb3J0ZXphcHJvamVjdC5vcmciLCJqdGkiOiJNVEMyWU1WSE1EQ1ROMlpJTkkwWllUTEtMV0pKTlRVVE5KVTVNRE00TkpVWk1UUTMiLCJyb2xlcyI6WyI0MjY2MzQ4MDM4NDUxMzYzODUiXSwic2NvcGUiOiJwcm9maWxlIGFwaSIsInN1YiI6IjQyNjYzNDgwMzg0Nzg4ODg5NyJ9.QE5yv40sssoo94alvdamunY6691ow0sRHzsZa3FxG7dpTKhXVfjzX-OknZ-2-p7ix9cFXt5_4HFBLi5peWXlVw",
#                      "429540262432276481",
#                      "brand-test")


# create_corteza_module("https://corteza1.phatle.dev",
#                       "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6IjQyNjYzNDgwMzg0NzYyNjc1MyIsImV4cCI6MTczOTQ0MDI5MiwiaWF0IjoxNzM5NDMzMDkyLCJpc3MiOiJjb3J0ZXphcHJvamVjdC5vcmciLCJqdGkiOiJNWlkwWkdGSE9ESVRaSk0xTUkwWllUWVdMV0laWVdRVE1aSTFZTVpMTVRCS01HVTUiLCJyb2xlcyI6WyI0MjY2MzQ4MDM4NDUxMzYzODUiXSwic2NvcGUiOiJwcm9maWxlIGFwaSIsInN1YiI6IjQyNjYzNDgwMzg0Nzg4ODg5NyJ9.SqRaRtP8bvfMjEwZvFC0Y4ULCaNY6VFpS7iMGfXmrpPwZ1clli_AgvwTyhlojY3QOeP3QTzFT2r87YUibGbghg",
#                       "429540262432276481",
#                       "lazada brands",
#                       "lazada-brands")