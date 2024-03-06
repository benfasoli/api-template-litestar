from dataclasses import dataclass

from litestar import get


@dataclass
class GetIndexResponseDTO:
    message: str


@get(path="/")
async def get_index() -> GetIndexResponseDTO:
    return GetIndexResponseDTO(message="🚀")


handlers = [get_index]
