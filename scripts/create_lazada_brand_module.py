import requests
import json

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


# check_corteza_module("https://corteza1.phatle.dev",
#                      "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6IjQyNjYzNDgwMzg0NzYyNjc1MyIsImV4cCI6MTczOTQyOTg5OSwiaWF0IjoxNzM5NDIyNjk5LCJpc3MiOiJjb3J0ZXphcHJvamVjdC5vcmciLCJqdGkiOiJNVEMyWU1WSE1EQ1ROMlpJTkkwWllUTEtMV0pKTlRVVE5KVTVNRE00TkpVWk1UUTMiLCJyb2xlcyI6WyI0MjY2MzQ4MDM4NDUxMzYzODUiXSwic2NvcGUiOiJwcm9maWxlIGFwaSIsInN1YiI6IjQyNjYzNDgwMzg0Nzg4ODg5NyJ9.QE5yv40sssoo94alvdamunY6691ow0sRHzsZa3FxG7dpTKhXVfjzX-OknZ-2-p7ix9cFXt5_4HFBLi5peWXlVw",
#                      "429540262432276481",
#                      "brand-test")


# create_corteza_module("https://corteza1.phatle.dev",
#                       "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6IjQyNjYzNDgwMzg0NzYyNjc1MyIsImV4cCI6MTczOTQ0MDI5MiwiaWF0IjoxNzM5NDMzMDkyLCJpc3MiOiJjb3J0ZXphcHJvamVjdC5vcmciLCJqdGkiOiJNWlkwWkdGSE9ESVRaSk0xTUkwWllUWVdMV0laWVdRVE1aSTFZTVpMTVRCS01HVTUiLCJyb2xlcyI6WyI0MjY2MzQ4MDM4NDUxMzYzODUiXSwic2NvcGUiOiJwcm9maWxlIGFwaSIsInN1YiI6IjQyNjYzNDgwMzg0Nzg4ODg5NyJ9.SqRaRtP8bvfMjEwZvFC0Y4ULCaNY6VFpS7iMGfXmrpPwZ1clli_AgvwTyhlojY3QOeP3QTzFT2r87YUibGbghg",
#                       "429540262432276481",
#                       "lazada brands",
#                       "lazada-brands")