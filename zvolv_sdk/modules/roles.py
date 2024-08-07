import json
import urllib.parse
import requests


class Roles:
    def __init__(self, session, logger, base_url):
        self.session = session
        self.logger = logger
        self.base_url = base_url
        self.workspace_instance = None

    def createRoles(self, rolesPayload: list):
        """
        Create roles.

        :param rolesPayload: [
                {
                    'GroupName': 'Role_Name',
                    'GroupDesc' : 'Role_Description'
                }
            ]
        :return: A response indicating the success or failure of the operation.
        """
        try:
            url = f"{self.base_url}/rest/v13/roles"
            response = self.session.post(url, json=rolesPayload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"Roles have been successfully created.")
            else:
                raise ValueError(resp.get('message'))
            return resp
        except requests.exceptions.RequestException as http_err:
            error_response = response.json()
            status_code = error_response.get('statusCode', response.status_code)
            error_message = error_response.get('message', str(http_err))

            error_message = f"{status_code} Error: {error_message}"
            self.logger.error(f"An error occurred: {error_message}")
            raise requests.exceptions.HTTPError(error_message)
        except Exception as e:
            self.logger.error(e)
            raise e

    def editRoles(self, rolesPayload: list):
        """
        Edit roles.

        :param rolesPayload: {
                'Role_ID': {
                    'GroupName': 'Role_Name',
                    'GroupDesc' : 'Role_Description'
                }
            }
        :return: A response indicating the success or failure of the operation.
        """
        try:
            url = f"{self.base_url}/rest/v13/roles"
            response = self.session.put(url, json=rolesPayload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"Roles have been successfully edited.")
            else:
                raise ValueError(resp.get('message'))
            return resp
        except requests.exceptions.RequestException as http_err:
            error_response = response.json()
            status_code = error_response.get('statusCode', response.status_code)
            error_message = error_response.get('message', str(http_err))

            error_message = f"{status_code} Error: {error_message}"
            self.logger.error(f"An error occurred: {error_message}")
            raise requests.exceptions.HTTPError(error_message)
        except Exception as e:
            self.logger.error(e)
            raise e

    def getRolesDetail(self, rolesPayload: list):
        """
        Get roles detail.

        :param rolesPayload: A list of role names (e.g., ['Role1', 'Role2', ...]).
        :return: A list of dictionaries with the following keys:
            {
                'GroupID',
                'GroupName',
                'GroupDesc',
                'GroupImageurl',
                'GroupType',
                'IsRole',
                'ImmediateParents',
                'ImmediateChildren',
                'Users'
            }
        """
        try:
            filter_dict = {"filter": json.dumps([{"operator": "IN", "column": "GroupName", "value": rolesPayload}])}
            # Encoding the filter dictionary into query parameters
            filter_params = urllib.parse.urlencode(filter_dict)
            url = f"{self.base_url}/rest/v13/roles?{filter_params}"
            response = self.session.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"Successfully retrieved roles ID.")
            else:
                raise ValueError(resp.get('message'))
            return resp["data"]
        except requests.exceptions.RequestException as http_err:
            error_response = response.json()
            status_code = error_response.get('statusCode', response.status_code)
            error_message = error_response.get('message', str(http_err))

            error_message = f"{status_code} Error: {error_message}"
            self.logger.error(f"An error occurred: {error_message}")
            raise requests.exceptions.HTTPError(error_message)
        except Exception as e:
            self.logger.error(e)
            raise e
