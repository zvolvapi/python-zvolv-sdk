# Examples using zvolv_sdk


## Submissions

### Post Submission
```python
from zvolv_sdk.models.submission import Submission

submission = Submission(
    formId="form_id",
    elements=[
        {
            "label": "field_name",
            "value": "field_value"
        }
    ]
)
response = client.submissions.post(submission)
client.logger.info(response)
```

### Get Submission
```python
id = "form_submission_id"
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
    Q('term', Name1='Hello Nish 2'),
    Q('term', Name2='Put operation check')
])
search_obj = search_obj.query(bool_query)

formID = "form_id"
response = client.submissions.search(formID, search_obj)
client.logger.info(response)
```

### Put Submission
```python
from zvolv_sdk.models.submission import Submission

submission = Submission(
    id="form_submission_id",
    elements=[
        {
            "label": "field_name",
            "value": "field_value"
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
    "variable_1": "value_1",
    "variable_2": "value_2"
}
response = client.document.getCustomTemplateData(templateId, variable)
client.logger.info(response)
```

### Get custom template doc HTML
```python
templateId = 1
variable = {
    "variable_1": "value_1",
    "variable_2": "value_2"
}
response = client.document.getCustomTemplateHtml(templateId, variable)
client.logger.info(response)
```



## Emails

### Send mail to roles
```python
roles = ["Role1", "Role2"]
subjectId = "custom_template_id"
messageId = "custom_template_id"
variables = {
    "Body": "My name is nishant"
}
response = client.communication.sendMailToRoles(roles, subjectId, messageId, variables)
client.logger.info(response)
```

### Send mail to emails
```python
emails = ["name1@email.com", "name2@email.com"]
subjectId = "custom_template_id"
messageId = "custom_template_id"
variables = {
    "Body": "My name is nishant"
}
response = client.communication.sendMailToEmails(emails, subjectId, messageId, variables)
client.logger.info(response)
```