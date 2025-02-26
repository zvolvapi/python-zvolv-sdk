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
from elasticsearch_dsl import Search

must_conditions = [
    # For partial/full-text search (case-insensitive, tokenized)
    # This will match any document that contains "Sharma" in the "Employee Name" field, 
    # regardless of case or word boundaries.
    {"match": {"Employee Name": "Nishant"}},
    
    # For exact match (case-sensitive, raw field)
    # This will match only exact "Sharma" in the "Employee Name" field as it uses the ".Keyword" 
    # field which is not analyzed and stores the value as-is.
    {"match": {"Employee Name.keyword": "Nishant"}} 
]

form_id = 'FORM_ID'
search_obj = Search().query("bool", must=must_conditions)
result = client.submissions.search(form_id=form_id, search_obj=search_obj)
print(result)
print(result["total_count"])


## FETCH MULTIPLE ENTRIES FROM Elasticsearch AND HANDLE PAGINATION.
# Specify how many records you want to fetch per page
page_size = 500  # Adjust this number based on your requirements

# Initialize the search object without conditions
search_obj = Search().extra(size=page_size)

# To handle pagination, we will loop through the pages until we reach the last page
page_number = 0
total_count = 0
all_results = []

while True:
    # Set the 'from' to handle pagination and 'size' to define the number of results per page
    search_obj = search_obj.extra(from_=page_number * page_size)

    # Perform the search
    result = client.submissions.search(form_id=form_id, search_obj=search_obj)

    # Extract the total count and elements
    total_count = result["total_count"]
    elements = result["elements"]

    # Append the current page's results to the all_results list
    all_results.extend(elements)

    # Break if there are no more results
    if len(elements) < page_size:
        break

    # Move to the next page
    page_number += 1

# After the loop, you have all the results in all_results
print(f"Total count: {total_count}")
print(f"Number of fetched elements: {len(all_results)}")
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
response = client.documents.get_custom_template_data(templateId, variable)
client.logger.info(response)
```

### Get custom template doc HTML
```python
templateId = 1
variable = {
    'VARIABLE_1': 'VALUE_1',
    'VARIABLE_2': 'VALUE_2'
}
response = client.documents.get_custom_template_html(templateId, variable)
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
response = client.communications.send_mail_to_roles(roles, subjectId, messageId, variables)
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
response = client.communications.send_mail_to_emails(emails, subjectId, messageId, variables)
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
response = client.roles.create_roles(rolesPayload)
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
response = client.roles.edit_roles(roles)
client.logger.info(response)
```

### Get roles details
```python
rolesPayload = ['ROLE_1', 'ROLE_2']
response = client.roles.get_roles_detail(rolesPayload)
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
response = client.users.create_users(userPayload)
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
response = client.users.edit_users(userPayload)
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
response = client.users.get_users(userPayload)
client.logger.info(response)
```



## Passwords

### Generate a random password.
```python
from zvolv_sdk.utility.passwords import generate_random_password

config = {
      "special": {"min": 2, "include": "@$#"},
      "upper": {"min": 2},
      "digits": {"min": 2},
      "lower": {"min": 2}
  }
pwd = generate_random_password(configuration=config)
client.logger.info(pwd)
```

### Hash a password using SHA-512.
```python
from zvolv_sdk.utility.passwords import password_encrypt_sha512

pwd = password_encrypt_sha512("Password@123")
client.logger.info(pwd)
```



## UserGroups

### Get details of a user group.
```python
group_id = "GROUP_ID"
response = client.usergroups.fetch_usergroup_by_id(group_id)
client.logger.info(response)
```

### Create Project.
```python
title = "FORM_TITLE"
formID = "FORM_ID"
form_input_data = {
    "FIELD_LABEL1": "FIELD_VALUE1",
    "FIELD_LABEL2": "FIELD_VALUE2"
}
response = client.workflows.create_project(title, "17503", form_input_data)
client.logger.info(response)
```



## Projects

### Fetch tasks metadata for a given workflow ID.
```python
wid = "WORK_FLOW_ID"
response = client.workflows.get_project_tasks_metadata(wid, filter)
client.logger.info(response)
```



## Files

### Upload a file and get URL.
```python
file_name = "FILE_NAME"
file_path = "FILE_PATH"
response = client.files.upload_file(file_name, file_path)
client.logger.info(response)
```

### Generate file upload metadata/element.
```python
absolute_file_path = "FILE_PATH"
file_url = "FILE_URL"
# NOTE: Provide either 'absolute_file_path' or 'file_url'
response = client.files.get_file_upload_element(absolute_file_path, file_url)
client.logger.info(response)
```
