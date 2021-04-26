from GitRepos.data import ui_data
from GitRepos.ui_operations import UIOps



class UIimpl:

    @staticmethod
    def get_repos_names():
        repos = UIOps().get_elements(ui_data.locator_XPATH, ui_data.all_repos)
        repos_content = []
        for repo in repos:
            repos_content.append(repo.text)
        return repos_content

