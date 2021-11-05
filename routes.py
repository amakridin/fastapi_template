from fastapi import APIRouter, Depends, Header, HTTPException
from handler import foo_bar
from types_validator import FooBar, Pong, CommonParameters

X_AUTH_TOKEN = "test"


async def verify_token(x_auth_token: str = Header(...)):
    if x_auth_token != X_AUTH_TOKEN:
        raise HTTPException(status_code=400, detail="X-Auth-Token header invalid")

router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/ping", response_model=Pong)
def ping() -> Pong:
    return Pong()


@router.get("/foo_bar/{endpoint}", response_model=FooBar)
async def fb(foo: str, bar: int, endpoint: str) -> FooBar:
    return await foo_bar(foo, bar, endpoint)


@router.get("/common_parameters/")
async def read_items(commons: CommonParameters = Depends(CommonParameters)) -> CommonParameters:
    return commons
