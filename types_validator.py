from pydantic import BaseModel, Field
from typing import Literal


class Pong(BaseModel):
    result: str = Field(default="pong", title="ping result",)


class FooBar(BaseModel):
    foo: str
    bar: int
    endpoint: Literal["ep1", "ep2", "ep3"]


class CommonParameters(BaseModel):
    query: str
    limit: int
    offset: int
