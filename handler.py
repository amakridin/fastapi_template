from types_validator import FooBar
from typing import Optional
from fastapi import Request


async def foo_bar(foo: str, bar: int, endpoint: Optional[str]) -> FooBar:
    return FooBar(foo=foo, bar=bar, endpoint=endpoint)
