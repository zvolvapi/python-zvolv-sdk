import requests

from ..models.form import Form
from ..utility.decorators import enforce_pydantic_model

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
    
    @enforce_pydantic_model(Form)
    def put(self, form: Form, enableRetrofit: bool = False, enableReSync: bool = False):
        """Update existing form"""
        # id or uuid field is required in the form model to update the form
        if not form.id and not form.uuid:
            raise ValueError("id or uuid field is required to update the form")
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
    
    @enforce_pydantic_model(Form)
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