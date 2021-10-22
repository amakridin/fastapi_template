from pydantic import BaseModel


class FooBar(BaseModel):
    foo: str
    bar: int
