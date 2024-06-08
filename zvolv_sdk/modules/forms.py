from typing import List, Optional
import requests
from pydantic import BaseModel

class Form(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    icon: str
    color: str
    type: str
    elements: str
    schemaVersion: str
    allowDraft: Optional[bool] = False
    setDraftInterval: int
    allowDraftNotPassed: Optional[bool] = False
    enableRetrofit: Optional[bool] = True
    enableReSync: Optional[bool] = True
    abacOperator: str
    tags: Optional[List] = []
    canReadRoles: Optional[List] = []
    canUpdateRoles: Optional[List] = []
    elements: Optional[List] = []


#     {
  
#   "elements": [
#     {
#       "elementId": "string",
#       "label": "string",
#       "type": "EDIT_TEXT",
#       "defaultValue": {},
#       "required": true,
#       "disabled": true,
#       "hidden": true,
#       "unique": true,
#       "updateIfUnique": true,
#       "properties": {},
#       "attributes": {},
#       "dependencies": {},
#       "validations": {},
#       "dataType": "INT",
#       "rbacConf": {
#         "canReadElementRoles": [
#           0
#         ],
#         "canUpdateElementRoles": [
#           0
#         ]
#       },
#       "abacConf": {
#         "canReadSubmissionAttributes": [
#           "string"
#         ],
#         "canUpdateSubmissionAttributes": [
#           "string"
#         ]
#       },
#       "showLabel": true,
#       "id": "string"
#     }
#   ],
  
#   "configurations": {},
 
# }
    


class Forms:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.workspace_instance = None
    
    def get(self, id):
        """Get form details from id."""
        url = f"{self.base_url}/api/v1/forms/{id}"
        response = self.session.get(url)
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                return Form(**resp['data']['elements'][0])
            else:
                print("Form get Failed")
                print(response.json())

        return response.json()
    
    def put(self, id):
        """Get form details from id."""
        url = f"{self.base_url}/api/v1/forms/{id}"
        response = self.session.put(url)
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                return resp['data']
            else:
                print("Form put Failed")
                print(response.json())

        return response.json()