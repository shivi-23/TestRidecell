from GitRepos.ui_operations import UIOps
import pytest


@pytest.fixture(scope="module")
def set_up():
    UIOps().open_browser()
    yield
    UIOps().close_browser()