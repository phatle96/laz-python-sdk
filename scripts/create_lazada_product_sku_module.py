import requests
import json


def create_lazada_product_sku_module(cortezaBaseUrl, connectionID, token, namespaceID, moduleName, moduleHandle):

    url = f"{cortezaBaseUrl}/api/compose/namespace/{namespaceID}/module/"

    payload = json.dumps({
    "name": f"{moduleName}",
    "handle": f"{moduleHandle}",
    "config": {
        "dal": {
        "connectionID": f"{connectionID}",
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
        "name": "productId",
        "kind": "String",
        "label": "Product ID (item_id)",
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
        "name": "productName",
        "kind": "String",
        "label": "Product Name (attributes.name)",
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
        "name": "skuId",
        "kind": "String",
        "label": "SKU ID (skus[SkuId])",
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
        "name": "sellerSku",
        "kind": "String",
        "label": "Seller SKU (skus[SellerSku])",
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
        "name": "productUrl",
        "kind": "String",
        "label": "Product URL (skus[Url])",
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
        "name": "shopSku",
        "kind": "String",
        "label": "Shop SKU (skus[ShopSku])",
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
        "name": "status",
        "kind": "String",
        "label": "SKU Status (skus[Status])",
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
        "name": "price",
        "kind": "String",
        "label": "Price (skus[price])",
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
        "name": "specialPrice",
        "kind": "String",
        "label": "Special Price (skus[special_price])",
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
        "name": "specialFromDate",
        "kind": "String",
        "label": "Special Price From (skus[special_from_date])",
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
        "name": "specialToDate",
        "kind": "String",
        "label": "Special Price To (skus[special_to_date])",
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
        "name": "specialTimeFormat",
        "kind": "String",
        "label": "Special Price Time Format (skus[special_time_format])",
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
        "name": "quantity",
        "kind": "String",
        "label": "Quantity (skus[quantity])",
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
        "name": "packageWidth",
        "kind": "String",
        "label": "Package Width (cm) (skus[package_width])",
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
        "name": "packageHeight",
        "kind": "String",
        "label": "Package Height (cm) (skus[package_height])",
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
        "name": "packageLength",
        "kind": "String",
        "label": "Package Length (cm) (skus[package_length])",
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
        "name": "packageWeight",
        "kind": "String",
        "label": "Package Weight (kg) (skus[package_weight])",
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
        "name": "packageContent",
        "kind": "String",
        "label": "Package Content (skus[package_content])",
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
        "name": "variation",
        "kind": "String",
        "label": "Variations (skus[saleProp])",
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
        "name": "skuImage1",
        "kind": "String",
        "label": "SKU Image 1 (skus[Images[]])",
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
        "name": "skuImage2",
        "kind": "String",
        "label": "SKU Image 2 (skus[Images[]])",
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
        "name": "skuImage3",
        "kind": "String",
        "label": "SKU Image 3 (skus[Images[]])",
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
        "name": "skuImage4",
        "kind": "String",
        "label": "SKU Image 4 (skus[Images[]])",
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
        "name": "skuImage5",
        "kind": "String",
        "label": "SKU Image 5 (skus[Images[]])",
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
        "name": "skuImage6",
        "kind": "String",
        "label": "SKU Image 6 (skus[Images[]])",
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
        "name": "skuImage7",
        "kind": "String",
        "label": "SKU Image 7 (skus[Images[]])",
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
        "name": "skuImage8",
        "kind": "String",
        "label": "SKU Image 8 (skus[Images[]])",
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
    'Authorization': f'Bearer {token}',
    'Connection': 'keep-alive',
    'Content-Language': 'en',
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()
