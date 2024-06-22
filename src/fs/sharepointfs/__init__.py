"""Implementation Pyfilesystem2 for SharePoint."""

from __future__ import annotations
import importlib.metadata
import logging

from .opener import SharePointFSOpener
from ._sharepointfs import SharePointFS


logger = logging.getLogger(__name__)


def _get_package_metadata():
    try:
        # Since importlib.metadata.metadata("fs.sharepointfs") might not work
        # due to the way Python handles dots in package names,
        # you should use the package distribution name with dash:
        metadata = importlib.metadata.metadata(__package__.replace(".", "-"))
        return metadata.get("License"), metadata.get("Author"), metadata.get("Version")
    except importlib.metadata.PackageNotFoundError:
        logger.exception("Could not find package metadata.")
        return None, None, None


__all__ = ["SharePointFS", "SharePointFSOpener"]
__license__, __author__, __version__ = _get_package_metadata()
__copyright__ = "Copyright (c) 2024 foreverfaint@gmail.com"
