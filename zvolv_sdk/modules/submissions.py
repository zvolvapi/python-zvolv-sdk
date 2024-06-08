import requests

from ..utility.decorators import enforce_pydantic_model
from ..models.submission import Submission

class Submissions:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.workspace_instance = None
    
    def get(self, id):
        """Get form details from id"""
        url = f"{self.base_url}/api/v1/submissions/{id}"
        response = self.session.get(url)
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False and resp['data']['elements']:
                return Submission(**resp['data']['elements'][0])
            else:
                print("Form get Failed")
                print(response.json())

        return response.json()
    
    @enforce_pydantic_model(Submission)
    def put(self, submission: Submission, skipValidation: bool = False, skipAutomation: bool = True, skipFormulaValidation: bool = False):
        """Update existing submission"""
        if not submission.id:
            raise ValueError("id field is required to update the submission")
        
        if not submission.elements or submission.elements == []:
            raise ValueError("elements field with atleast 1 element is required to update the submission")
        
        url = f"{self.base_url}/api/v1/submissions/{submission.id}?skipValidation={skipValidation}&skipAutomation={skipAutomation}&skipFormulaValidation={skipFormulaValidation}"
        response = self.session.put(url, json=submission.model_dump())
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                return resp
            else:
                print("Form put Failed")
                print(response.json())

        return response.json()
    
    @enforce_pydantic_model(Submission)
    def post(self, submission: Submission, skipValidation: bool = False, skipAutomation: bool = True, skipFormulaValidation: bool = False):
        """Create a new submission"""
        if not submission.formId:
            raise ValueError("formId field is required to create the submission")
        
        if not submission.elements:
            raise ValueError("elements field is required to create the submission")
        
        url = f"{self.base_url}/api/v1/submissions?skipValidation={skipValidation}&skipAutomation={skipAutomation}&skipFormulaValidation={skipFormulaValidation}"
        response = self.session.post(url, json=submission.model_dump())
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                return resp
            else:
                print("Form post Failed")
                print(response.json())

        return response.json()