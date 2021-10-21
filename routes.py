from fastapi import APIRouter
from handler import foo_bar

router = APIRouter()


@router.get("/foo")
async def foo():
    return await foo_bar()
