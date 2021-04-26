from GitRepos.api import API
from GitRepos.data.api_data import toignore_keyword


class APIimpl:

    @staticmethod
    def get_all_repos_details():
        response = API().get_repos_request()
        rs = response.json()
        return rs

    def toignore_keyword(self):
        return toignore_keyword