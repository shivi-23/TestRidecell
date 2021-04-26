import pytest
from GitRepos.ui_impl import UIimpl
from GitRepos.api_impl import APIimpl


@pytest.mark.usefixtures('set_up')
class TestUIAPI:

    def test_correctness_of_repo_names_and_desc(self):
        repos_content = UIimpl().get_repos_names()
        actual_repos_names = []
        actual_repos_desc = []
        for repo in repos_content:
            repo_list = repo.split('\n')

            if '' in repo_list[0]:
                r = repo_list[0].split()
                repo_name = r[0]
            else:
                repo_name = repo_list[0]
            if APIimpl().toignore_keyword() in repo_list[1]:
                repo_desc = repo_list[2]
            else:
                repo_desc = repo_list[1]
            actual_repos_names.append(repo_name)
            actual_repos_desc.append(repo_desc)
        repos_response = APIimpl().get_all_repos_details()
        for repo in repos_response:
            assert repo["name"] in actual_repos_names
            if repo["description"] is not None:
                assert repo["description"] in actual_repos_desc

