""" Contains some shared types for properties """
from typing import BinaryIO, Generic, MutableMapping, Optional, Tuple, TypeVar

import attr

# Instead of declaring a new Unset-Type, use a common version so that isinstance works properly
from ...common import types

Unset = types.Unset
UNSET = types.UNSET


FileJsonType = Tuple[Optional[str], BinaryIO, Optional[str]]


@attr.s(auto_attribs=True)
class File:
    """Contains information for file uploads"""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@attr.s(auto_attribs=True)
class Response(Generic[T]):
    """A response from an endpoint"""

    status_code: int
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


__all__ = ["File", "Response", "FileJsonType"]
