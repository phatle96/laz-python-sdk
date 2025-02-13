import requests
import json
import logging

def create_attribute_options_module(cortezaUrl, connectionId, cortezaBearerToken, cortezaNamespace, cortezaModuleName, cortezaModuleHandle):

  # cortezaModuleName = lazada attribute options
  # cortezaModuleHandle = lazada-attribute-options

  url = f"{cortezaUrl}/api/compose/namespace/{cortezaNamespace}/module/"

  payload = json.dumps({
  "name": f"{cortezaModuleName}",
  "handle": f"{cortezaModuleHandle}",
  "config": {
    "dal": {
      "connectionID": f"{connectionId}",
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
      "name": "en_name",
      "kind": "String",
      "label": "EN Name",
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
      "name": "id",
      "kind": "String",
      "label": "Option ID",
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
  