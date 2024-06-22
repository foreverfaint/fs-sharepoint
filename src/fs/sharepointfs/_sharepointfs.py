"""Manage SharePoint folders and files as a file system."""

from __future__ import annotations

from typing import BinaryIO, Collection, Mapping, Any, TYPE_CHECKING


from fs.base import FS
from fs import errors
from office365.sharepoint.client_context import (
    ClientContext,
    UserCredential,
    ClientCredential,
)


if TYPE_CHECKING:
    # Unused imports add a performance overhead at runtime,
    # and risk creating import cycles.
    # If an import is only used in typing-only contexts,
    # it can instead be imported conditionally under an if TYPE_CHECKING:
    # block to minimize runtime overhead.
    from fs.info import Info
    from fs.permissions import Permissions
    from fs.subfs import SubFS


class SharePointFS(FS):
    def __init__(
        self,
        site_url: str,
        ctx: ClientContext | None = None,
        username: str | None = None,
        password: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        proxy_host: str | None = None,
        proxy_port: int | None = None,
        environment: str | None = None,
        *args,
        **kwargs,
    ) -> None:
        """Implementation of a file system that interacts with SharePoint.

        Args:
            site_url: The URL of the SharePoint site.
            ctx: The client context to use for SharePoint operations. \
                There are many ways to create a client context, \
                we expose this parameter to allow for flexibility.
            username: The username to use for authentication.
            password: The password to use for authentication.
            client_id: The client ID to use for authentication.
            client_secret: The client secret to use for authentication.
            proxy_host: The host of the proxy server to use.
            proxy_port: The port of the proxy server to use.
            environment: The environment to use for authentication.
            args: Additional arguments to pass to the base
            kwargs: Additional keyword arguments to pass to the base.
        """
        super().__init__(*args, **kwargs)

        self._site_url = site_url

        if ctx is None:
            if username is not None and password is not None:
                credential = UserCredential(username, password)

            if credential is None:
                if client_id is not None and client_secret is not None:
                    credential = ClientCredential(client_id, client_secret)

            if credential is None:
                raise errors.CreateFailed("No valid credentials provided.")

            ctx = ClientContext(self._site_url).with_credentials(credential, environment=environment)

        if ctx is None:
            raise errors.CreateFailed("No valid client context provided.")

        if proxy_host is not None and proxy_port is not None:
            proxy_url = f"http://{proxy_host}:{proxy_port}"

            def _set_proxy(req):
                req.proxies = {"http": proxy_url, "https": proxy_url}

            ctx.pending_request().beforeExecute += _set_proxy

        self._ctx = ctx

    def __repr__(self) -> str:
        # type: () -> str
        return f"SharePointFS({self._site_url})"

    def __str__(self) -> str:
        # type: () -> str
        return f"<{self.__class__.__name__}>"

    def getinfo(self, path: str, namespaces: Collection[str] | None = None) -> Info:
        return super().getinfo(path, namespaces)

    def listdir(self, path: str) -> list[str]:
        return super().listdir(path)

    def makedir(self, path: str, permissions: Permissions | None = None, recreate: bool = False) -> SubFS[FS]:
        return super().makedir(path, permissions, recreate)

    def openbin(self, path: str, mode: str = "r", buffering: int = -1, **options: Any) -> BinaryIO:
        return super().openbin(path, mode, buffering, **options)

    def remove(self, path: str) -> None:
        return super().remove(path)

    def removedir(self, path: str) -> None:
        return super().removedir(path)

    def setinfo(self, path: str, info: Mapping[str, Mapping[str, object]]) -> None:
        return super().setinfo(path, info)
