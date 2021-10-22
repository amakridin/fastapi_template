from fastapi import APIRouter
from handler import foo_bar

router = APIRouter()


@router.get("/foo_bar")
async def fb(foo: str, bar: int):
    return await foo_bar(foo, bar)
