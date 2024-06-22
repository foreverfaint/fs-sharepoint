from fs.sharepointfs import SharePointFS


def test_SharePointFS_with_user_credentials(
    setup_SharePoint_Web, mock_SharePoint_site_url, mock_SharePoint_username, mock_SharePoint_password
):
    fs_ = SharePointFS(
        mock_SharePoint_site_url,
        username=mock_SharePoint_username,
        password=mock_SharePoint_password,
    )
    print(dir(fs_._ctx))
    assert fs_._ctx is not None


def test_SharePointFS_with_client_credentials(
    setup_SharePoint_Web, mock_SharePoint_site_url, mock_SharePoint_username, mock_SharePoint_password
):
    fs_ = SharePointFS(
        mock_SharePoint_site_url,
        username=mock_SharePoint_username,
        password=mock_SharePoint_password,
    )
    assert fs_._ctx is not None
