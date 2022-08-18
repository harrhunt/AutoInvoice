import requests


class Clockify:
    base_url = 'https://api.clockify.me/api/v1/'
    current_workspace = None
    current_user = None
    current_project = None

    def __init__(self, api_key, workspace=None, user=None, project=None):
        self.api_key = api_key
        self.current_workspace = workspace
        self.current_user = user
        self.current_project = project
        self.headers = {"X-Api-Key": api_key}

    def _get_json_request(self, url, params=None):
        if params is None:
            params = {}
        r = requests.get(url, params=params, headers=self.headers)
        return r.json()

    def _check_workspace(self, workspace):
        if workspace:
            self.current_workspace = workspace
        if not self.current_workspace:
            raise ValueError

    def _check_user(self, user):
        if user:
            self.current_user = user
        if not self.current_user:
            raise ValueError

    def _check_project(self, project):
        if project:
            self.current_project = project
        if not self.current_project:
            raise ValueError

    def get_workspaces(self):
        return self._get_json_request(f"{self.base_url}workspaces")

    def get_users(self, workspace=None, params=None):
        if params is None:
            params = {}
        self._check_workspace(workspace)
        return self._get_json_request(f"{self.base_url}workspaces/{self.current_workspace}/users", params)

    def get_projects(self, workspace=None, params=None):
        if params is None:
            params = {}
        self._check_workspace(workspace)
        if self.current_workspace:
            return self._get_json_request(f"{self.base_url}workspaces/{self.current_workspace}/projects", params)

    def get_time_entries(self, workspace=None, user=None, params=None):
        if params is None:
            params = {}
        self._check_workspace(workspace)
        self._check_user(user)
        return self._get_json_request(
            f"{self.base_url}/workspaces/{self.current_workspace}/user/{self.current_user}/time-entries",
            params
        )

    def get_active_projects(self, workspace=None):
        return self.get_projects(workspace, {"archived": False})

    def get_project_by_name(self, name, workspace=None):
        projects = self.get_projects(workspace)
        for project in projects:
            if project["name"] == name:
                return project
        return None
