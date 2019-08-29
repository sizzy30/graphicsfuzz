# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from gfauto.common_pb2 import (
    ArchiveSet as gfauto___common_pb2___ArchiveSet,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Recipe(google___protobuf___message___Message):

    @property
    def download_and_extract_archive_set(self) -> RecipeDownloadAndExtractArchiveSet: ...

    def __init__(self,
        download_and_extract_archive_set : typing___Optional[RecipeDownloadAndExtractArchiveSet] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Recipe: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"download_and_extract_archive_set",u"recipe"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"download_and_extract_archive_set",u"recipe"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"download_and_extract_archive_set",b"download_and_extract_archive_set",u"recipe",b"recipe"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"download_and_extract_archive_set",b"recipe"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"recipe",b"recipe"]) -> typing_extensions___Literal["download_and_extract_archive_set"]: ...

class RecipeDownloadAndExtractArchiveSet(google___protobuf___message___Message):

    @property
    def archive_set(self) -> gfauto___common_pb2___ArchiveSet: ...

    def __init__(self,
        archive_set : typing___Optional[gfauto___common_pb2___ArchiveSet] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeDownloadAndExtractArchiveSet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"archive_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"archive_set"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"archive_set",b"archive_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"archive_set"]) -> None: ...