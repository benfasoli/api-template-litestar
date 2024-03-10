from dataclasses import dataclass

from litestar import Router, get


@dataclass
class GetIndexResponseDTO:
    message: str


@get(path="/")
async def get_index() -> GetIndexResponseDTO:
    return GetIndexResponseDTO(message="🚀")


router = Router(path="/", route_handlers=[get_index])
