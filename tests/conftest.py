import os

import pytest
from office365.sharepoint.webs import web


@pytest.fixture(autouse=True, scope="session")
def _echo_envvars():
    print(f"\nDEBUG={os.environ.get('DEBUG')}")


@pytest.fixture()
def setup_SharePoint_Web(mocker):
    mocker.spy(web.Web, "get")
    mocker.spy(web.Web, "get_folder_by_server_relative_url")
    mocker.spy(web.Web, "get_file_by_server_relative_url")
    mocker.spy(web.Web, "ensure_folder_path")
    mocker.patch.object(web.Web, "execute_query", autospec=True)
    yield web.Web


@pytest.fixture()
def mock_SharePoint_site_url():
    return "https://example.sharepoint.com/sites/ExampleSite"


@pytest.fixture()
def mock_SharePoint_username():
    return "SharePointUsername"


@pytest.fixture()
def mock_SharePoint_password():
    return "SharePointPassword"
