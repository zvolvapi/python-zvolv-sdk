import requests

from .modules.workspace import Workspace
from .modules.auth import Auth

class ZvolvClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self._workspace_module = None
        self._auth_module = None

    @property
    def workspace(self):
        if not self._workspace_module:
            self._workspace_module = Workspace(self.session, self.base_url)
        return self._workspace_module
    
    @property
    def auth(self):
        if not self._workspace_module or not self._workspace_module.workspace_instance:
            raise Exception('Workspace not initialized! Please use workspace.init() before calling auth methods')
        if not self._auth_module:
            self._auth_module = Auth(self.session, self.base_url, self._workspace_module.workspace_instance)
        return self._auth_module