from typing import List, Optional, Union
import requests
from pydantic import BaseModel

class Element(BaseModel):
    elementId: str
    label: str
    type: str
    defaultValue: Optional[Union[str, bool, int, dict, list]] = None
    required: Optional[bool] = True
    disabled: Optional[bool] = True
    hidden: Optional[bool] = True
    unique: Optional[bool] = True
    updateIfUnique: Optional[bool] = True
    properties: Optional[dict] = {}
    attributes: Optional[dict] = {}
    dependencies: Optional[List] = []
    validations: Optional[List] = []
    dataType: str
    rbacConf: Optional[dict] = {}
    abacConf: Optional[dict] = {}
    showLabel: Optional[bool] = True
    id: str

class Form(BaseModel):
    id: str
    uuid: str
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
    configurations: Optional[dict] = {}
    elements: List[Element] = []

class Forms:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.workspace_instance = None
    
    def get(self, id):
        """Get form details from id"""
        url = f"{self.base_url}/api/v1/forms/{id}"
        response = self.session.get(url)
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False and resp['data']['elements']:
                return Form(**resp['data']['elements'][0])
            else:
                print("Form get Failed")
                print(response.json())

        return response.json()
    
    def put(self, form: Form, enableRetrofit: bool = False, enableReSync: bool = False):
        """Update existing form"""
        url = f"{self.base_url}/api/v1/forms?enableRetrofit={enableRetrofit}&enableReSync={enableReSync}"
        response = self.session.put(url, json=form.model_dump())
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                return resp
            else:
                print("Form put Failed")
                print(response.json())

        return response.json()
    
    def post(self, form: Form):
        """Create a new form"""
        url = f"{self.base_url}/api/v1/forms"
        response = self.session.post(url, json=form.model_dump())
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                return resp
            else:
                print("Form post Failed")
                print(response.json())

        return response.json()