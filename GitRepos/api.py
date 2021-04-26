import requests
from GitRepos.data import api_data


class API:

    @staticmethod
    def get_repos_request():
        response = requests.get(api_data.org_repo_url, verify=False)
        return response

