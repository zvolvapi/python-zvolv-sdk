# Examples using zvolv_sdk

## Forms

### Create a new Form
```python
from zvolv_sdk import ZvolvClient
from zvolv_sdk.models.form import Form

base_url = 'your-zvolv-base-url'
client = ZvolvClient(base_url)

domain = 'your-zvolv-workspace-domain'
client.workspace.init(domain)

email = 'your-zvolv-workspace-user-email'
password = 'your-zvolv-workspace-user-password'
client.auth.login(email, password)

form = Form(
    title="Employee Data Import",
    description="Employee Data Import Form",
    icon="rise",
    type="MASTER",
    color="#f31d2f",
    schemaVersion="v1",
    allowDraft=False,
    setDraftInterval=0,
    configurations={},
    abacOperator="OR",
    tags=[],
    canReadRoles=[-1],
    canUpdateRoles=[-1],
    elements=[
        {
             "required": False,
                "defaultValue": None,
                "type": "EDIT_TEXT",
                "label": "Name",
                "elementId": "EID_c3u82fkx7y",
                "hidden": False,
                "unique": False,
                "updateIfUnique": False,
                "properties": {
                    "hideLabel": False
                },
                "attributes": {},
                "dependencies": [],
                "validations": [],
                "dataType": "STRING",
                "rbacConf": {},
                "abacConf": {},
                "showLabel": True,
                "indexColumnId": 0
        },
            {
                "required": False,
                "defaultValue": None,
                "type": "EDIT_TEXT",
                "label": "Age",
                "elementId": "EID_hqw7k58523",
                "hidden": False,
                "unique": False,
                "updateIfUnique": False,
                "properties": {
                    "hideLabel": False
                },
                "attributes": {},
                "dependencies": [],
                "validations": [],
                "dataType": "STRING",
                "rbacConf": {},
                "abacConf": {},
                "showLabel": True,
                "indexColumnId": 0
            },
            {
                "required": False,
                "defaultValue": None,
                "type": "EDIT_TEXT",
                "label": "City",
                "elementId": "EID_ozpxobcklo",
                "hidden": False,
                "unique": False,
                "updateIfUnique": False,
                "properties": {
                    "hideLabel": False
                },
                "attributes": {},
                "dependencies": [],
                "validations": [],
                "dataType": "STRING",
                "rbacConf": {},
                "abacConf": {},
                "showLabel": True,
                "indexColumnId": 0
            }
    ]
)

response = client.forms.post(form)
print(response)
```