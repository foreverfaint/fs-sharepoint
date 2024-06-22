from __future__ import annotations
from typing import ClassVar, AnyStr

from fs.opener import Opener, registry

from ._sharepointfs import SharePointFS


class SharePointFSOpener(Opener):
    protocols: ClassVar[list[AnyStr]] = ["sharepoint"]

    def open_fs(self, fs_url: AnyStr, parse_result, writeable: bool, create: bool, cwd: AnyStr) -> AnyStr:
        return SharePointFS(
            parse_result.resource,  # site_url
            username=parse_result.username,
            password=parse_result.password,
        )


registry.install(SharePointFSOpener)
