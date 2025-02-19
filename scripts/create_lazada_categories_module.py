import requests
import json

def create_category_module(cortezaUrl, connectionId, cortezaBearerToken, cortezaNamespace, cortezaModuleName, cortezaModuleHandle):

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
      "name": "category_id",
      "kind": "String",
      "label": "Category ID",
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
      "name": "var",
      "kind": "Bool",
      "label": "Var",
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
        "trueLabel": "",
        "falseLabel": "",
        "switch": False
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
      "name": "leaf",
      "kind": "Bool",
      "label": "Leaf",
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
        "trueLabel": "",
        "falseLabel": "",
        "switch": False
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
      "name": "path",
      "kind": "String",
      "label": "Path",
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
  
