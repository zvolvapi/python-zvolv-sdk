import requests
import urllib.parse
import json


class Workflows:
    def __init__(self, session, logger, base_url):
        self.session = session
        self.logger = logger
        self.base_url = base_url
        self.workspace_instance = None

    def get_project_tasks_metadata(self, wid: str, filters: dict = None):
        """
        Fetch metadata for tasks within a workflow ID, applying optional filters.

        :param wid: Workflow ID for which task details are being retrieved.
        :param filters: Optional dictionary to filter tasks, including:
            - "stageCodes": List of specific stage codes.
            - "status": List of task statuses (e.g., "Active", "Assigned").
            - "department": List of departments to filter by (e.g., "DepartmentA/TagA", "DepartmentB/TagB").
        :return: List of task metadata.
        """
        if filters is None:
            filters = {}
        try:
            if filters:
                filter_dict = {'filter': json.dumps(filters)}
                # Encoding the filter dictionary into query parameters
                filter_params = urllib.parse.urlencode(filter_dict)
                url = f"{self.base_url}/rest/v13/tasks/wormgraph/workflow/{wid}?{filter_params}"
            else:
                url = f"{self.base_url}/rest/v13/tasks/wormgraph/workflow/{wid}"
            response = self.session.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            resp = response.json()
            if resp.get('error') is False:
                self.logger.info(f"Successfully fetched tasks for WorkflowID {wid}")
            else:
                raise ValueError(resp.get('message'))
            return resp['data']['tasks']

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

