from types_validator import FooBar


async def foo_bar(foo: str, bar: int):
    return FooBar(foo=foo, bar=bar).dict()
