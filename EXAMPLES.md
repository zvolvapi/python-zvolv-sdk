# Examples using zvolv_sdk

> **NOTES:**
> 1. Text that is not capitalized (e.g., elementId, value) represents static parts of the payload and should be left unchanged.
> 2. Replace capitalized placeholders such as FORM_ID, FIELD_LABEL, and FIELD_VALUE with the actual values relevant to your specific use case.


## Submissions

### Post Submission
```python
from zvolv_sdk.models.submission import Submission

submission = Submission(
    formId='FORM_ID',
    elements=[
        # Use either label or elementId in each element dictionary, but not both.
        {
            'label': 'FIELD_LABEL',     # Pass field label here
            'value': 'FIELD_VALUE'
        },
        {
            'elementId': 'FIELD_ELEMENT_ID',    # Pass field elementId here
            'value': 'FIELD_VALUE'
        }
    ]
)
response = client.submissions.post(submission)
client.logger.info(response)
```

### Get Submission
```python
id = 'FORM_SUBMISSION_ID'
response = client.submissions.get(id)
client.logger.info(response)
```

### Search Operation
```python
from elasticsearch_dsl import Q, Search

# term - Q('term', field='exact value')
# terms - Q('terms', field=['value1', 'value2'])
# match - Q('match', field='search text')

search_obj = Search()
bool_query = Q('bool', must=[
    Q('term', FIELD_LABEL1='FIELD_VALUE1'),
    Q('term', FIELD2_LABEL2='FIELD_VALUE2')
])
search_obj = search_obj.query(bool_query)

formID = 'FORM_ID'
response = client.submissions.search(formID, search_obj)
client.logger.info(response)
```

### Put Submission
```python
from zvolv_sdk.models.submission import Submission

submission = Submission(
    id='FORM_SUBMISSION_ID',
    elements=[
        # Use either label or elementId in each element dictionary, but not both.
        {
            'label': 'FIELD_LABEL',     # Pass field label here
            'value': 'FIELD_VALUE'
        },
        {
            'elementId': 'FIELD_ELEMENT_ID',    # Pass field elementId here
            'value': 'FIELD_VALUE'
        }
    ]
)
response = client.submissions.put(submission)
client.logger.info(response)
```



## Documents

### Get custom template doc data
```python
templateId = 1
variable = {
    'VARIABLE_1': 'VALUE_1',
    'VARIABLE_2': 'VALUE_2'
}
response = client.document.getCustomTemplateData(templateId, variable)
client.logger.info(response)
```

### Get custom template doc HTML
```python
templateId = 1
variable = {
    'VARIABLE_1': 'VALUE_1',
    'VARIABLE_2': 'VALUE_2'
}
response = client.document.getCustomTemplateHtml(templateId, variable)
client.logger.info(response)
```



## Emails

### Send mail to roles
```python
roles = ['ROLE_1', 'ROLE_2']
subjectId = 'CUSTOM_TEMPLATE_ID'
messageId = 'CUSTOM_TEMPLATE_ID'
variables = {
    'Body': 'My name is nishant'
}
response = client.communication.sendMailToRoles(roles, subjectId, messageId, variables)
client.logger.info(response)
```

### Send mail to emails
```python
emails = ['name1@email.com', 'name2@email.com']
subjectId = 'CUSTOM_TEMPLATE_ID'
messageId = ' CUSTOM_TEMPLATE_ID'
variables = {
    'Body': 'My name is nishant'
}
response = client.communication.sendMailToEmails(emails, subjectId, messageId, variables)
client.logger.info(response)
```



## Roles

### Create Role
```python
rolesPayload = [
    {
        'GroupName': 'ROLE_NAME',
        'GroupDesc' : 'ROLE_DESCRIPTION'
    }
]
response = client.roles.createRoles(rolesPayload)
client.logger.info(response)
```

### Edit Role
```python
roles = {
    'ROLE_ID': {
        'GroupName': 'ROLE_NAME',
        'GroupDesc' : 'ROLE_DESCRIPTION'
    }
}
response = client.roles.editRoles(roles)
client.logger.info(response)
```

### Get roles details
```python
rolesPayload = ['ROLE_1', 'ROLE_2']
response = client.roles.getRolesDetail(rolesPayload)
client.logger.info(response)
```



## Users

### Create Users
```python
from zvolv_sdk.models.user import User
from zvolv_sdk.utility.passwords import password_encrypt_sha512

userPayload = []

user = User(
    Profile={
        'Title':  'USER_NAME',
        'Description': 'USER_DESCRIPTION',
        'UserEmail': 'USER_EMAIL',
        'UserPhone': 'USER_PHONE',
        'UserPassword': password_encrypt_sha512('Password@123'),
        'ProfilePic': 'IMAGE_URL',
    },
    Attributes=[
        {
            'isUser': False,
            'key': 'ATTRIBUTE_KEY',
            'value': [
                'ATTRIBUTE_VALUE'
            ]
        }
    ],
    Groups=[
        'ROLE_ID'
    ]
)
userPayload.append(user)
response = client.users.createUsers(userPayload)
client.logger.info(response)
print(response)
```

### Edit Users
```python
from zvolv_sdk.models.user import User
from zvolv_sdk.utility.passwords import password_encrypt_sha512

user = User(
    EncryptedZviceID= "USER_ENCRYPTION_ID",
    Profile={
        'UserID': 'USER_ID',
        'Title':  "USER_NAME",
        'Description': 'USER_DESCRIPTION',
        'UserEmail': 'USER_EMAIL',
        'UserPhone': 'USER_PHONE',
        'UserPassword': password_encrypt_sha512("Password@123"),
        'ProfilePic': 'IMAGE_URL'
    },
    # Attributes=[
    #     {
    #         'AttributeID': "ATTRIBUTE_ID",
    #         'isUser': False,
    #         'key': 'ATTRIBUTE_KEY',
    #         'value': [
    #             'ATTRIBUTE_VALUE'
    #         ]
    #     }
    # ],
    Groups=[
        "ROLE_ID"
    ]
)
userPayload = []
userPayload.append(user)
response = client.users.editUsers(userPayload)
client.logger.info(response)
```

### Get Users
```python
userPayload = [
    {
        "operator":"=",
        "value": "USER_EMAIL",
        "column": "UserEmail"   # Options: UserEmail, UserID, UserPhone  
    }
]
response = client.users.getUsers(userPayload)
client.logger.info(response)
```

