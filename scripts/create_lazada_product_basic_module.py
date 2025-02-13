import requests
import json


def create_lazada_product_basic_module(cortezaBaseUrl, connectionID, token, namespaceID, moduleName, moduleHandle):

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
        "name": "productNameMY",
        "kind": "String",
        "label": "Product Name In MY (attributes.name_ms)",
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
        "label": "Status (status)",
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
        "name": "image1",
        "kind": "String",
        "label": "Product Image 1 (image)",
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
        "name": "image2",
        "kind": "String",
        "label": "Product Image 2 (image)",
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
        "name": "image3",
        "kind": "String",
        "label": "Product Image 3 (image)",
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
        "name": "image4",
        "kind": "String",
        "label": "Product Image 4 (image)",
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
        "name": "image5",
        "kind": "String",
        "label": "Product Image 5 (image)",
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
        "name": "image6",
        "kind": "String",
        "label": "Product Image 6 (image)",
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
        "name": "image7",
        "kind": "String",
        "label": "Product Image 7 (image)",
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
        "name": "image8",
        "kind": "String",
        "label": "Product Image 8 (image)",
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
        "name": "warranty",
        "kind": "String",
        "label": "Warranty (attributes.warranty)",
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
        "name": "warrantyType",
        "kind": "String",
        "label": "Warranty Type (attributes.warranty_type)",
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
        "name": "warrantyPolicy",
        "kind": "String",
        "label": "Warranty Policy (attributes.product_warranty)",
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
        "name": "mainDescription",
        "kind": "String",
        "label": "Main Description (attributes.description)",
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
        "name": "shortDescription",
        "kind": "String",
        "label": "Short Description (attributes.short_description)",
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
