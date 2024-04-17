# FastApi

[패키지 검색](https://pypi.org/)

## 기본 설치 packages

- [fastapi](https://fastapi.tiangolo.com/)

  - FastApi
  - Query
  - Path
  - Body
  - Cookie
  - File
  - Header
  - status
  - Form
  - File
  - uploadFile
  - encoders
    - jsonable_encoder
  - HTTPException
  - exceptions
    - RequestValidationError
  - responses
    - JSONResponse
    - PlainTextResponse
    - HTMLResponse
  - exception_handlers
    - http_exception_handler
    - request_validation_exception_handler
  - Depends
  - security
    - OAuth2PasswordBearer
    - OAuth2PasswordRequestForm
    - SecurityScopes
    - HTTPBasic
    - HTTPBasicCredentials
  - Request
  - middleware
    - httpsredirect
      - HTTPSRedirectMiddleware
    - cors
      - CORSMiddleware
    - trustedhost
      - TrustedHostMiddleware
    - gzip
      - GZipMiddleware
  - testclient
    - TestClient

- [pydantic](https://docs.pydantic.dev/latest/)
  > Pydantic is the most widely used data validation library for Python
  - BaseModel
  - Field
  - HttpUrl
  - EmailStr
  - ValidationError
  - dataclasses
    - dataclass
- [starlette](https://www.starlette.io/)

  - exceptions
    - HTTPException
  - responses
    - HTMLResponse

<br />

## 기타 사용 packages

- [passlib](https://fastapi.tiangolo.com/ko/tutorial/security/oauth2-jwt/#install-passlib)
  - context
    - CryptContext
- [pydantic_settings](https://fastapi.tiangolo.com/ko/advanced/settings/?h=pydantic_settings#pydantic-settings)

  - BaseSettings
  - SettingsConfigDict

- [python-dotenv](https://fastapi.tiangolo.com/ko/advanced/settings/?h=python#reading-a-env-file)

- [jose](https://fastapi.tiangolo.com/ko/tutorial/security/oauth2-jwt/?h=jose#install-python-jose)

  - JWTError
  - jwt

<br />

## Swagger

### api

```python
@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    response_description="The created item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """

    return item
```

<br />

### Example Data

파라미터에서 지정 시

```python
item: Item = Body(example = {
  "name": "foo",
  "desc": "desc"
})
```

<br />

class인 경우

- 각각 지정 시

  ```python
  name: str = Field(examples=["Foo"])
  desc: str | None = Field(None, example="example data") # example 키워드 지원 종료 예정
  ```

- 한번에 지정 시

  ```python
  # 클래스 내부에서
  model_config = {
      "json_schema_extra": {
          "examples": [
              {
                  "name": "Foo",
                  "description": "A very nice Item",
                  "price": 35.4,
                  "tax": 3.2,
              }
          ]
      }
  }

  # 또는 Config 내부 클래스 추가 후, // example 키워드 지원 종료 예정
  class Config:
    schema_extra = {
      "example" : {
        "name": "foo",
        "description": "desc",
      }
    }

  # 또는
  item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
            }
        )
  ]
  ```

[여러개 지정 시 - examples](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)

<br />

## 의존성

### 경로 의존성

```python
@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
```

<br />

### 전역 의존성

```python
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
```

<br />

### 하위 의존성

> use_cache=True\
> 동일 요청에서 하위 의존성이 여러 번 호출되어도 최초에 가져온 값을 재사용

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from random import randint
from typing import Annotated

app = FastAPI()

def get_random_number():
    return randint(0, 100)

async def cached_dependency(value: Annotated[int, Depends(get_random_number, use_cache=True)]):
    return {"value": value}

@app.get("/cached")
async def cached():
    return await cached_dependency()  # 같은 난수가 리턴
```

<br />

## Database

- `commit`: 트랜잭션을 명시적으로 시작하지 않는 한, 세션이 개별 변경사항에 대해 즉시 자동으로 커밋
- `flush`: 세션의 변경사항을 데이터베이스에 임시로 반영, 트랜잭션은 아직 완료되지 않은 상태이므로 롤백이 가능
- `refresh`: 동일 세션에서 객체의 상태를 동기화 할 때 사용

```python
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

# SQLAlchemy ORM 인스턴스
db_user = get_user_from_database()  # 가정된 함수

# orm_mode 설정으로 인해 바로 Pydantic 모델로 변환 가능
user = User.from_orm(db_user)
```

<br />

### etc

```python
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

```python
class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db
```

<br />

## 인증

[참고](https://fastapi.tiangolo.com/ko/tutorial/security/oauth2-jwt/)

> python-multipart 필요 - "양식 데이터"를 사용하기 때문

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

<br />

## [테스트](https://fastapi.tiangolo.com/ko/advanced/async-tests/)

### 동시 요청

```python
import pytest
import asyncio
from httpx import AsyncClient

@pytest.mark.anyio
async def test_multiple_requests():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        tasks = [ac.get("/") for _ in range(100)]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            assert response.status_code == 200
```

<br />

## ETC

### env

> For this to work, you need to pip install python-dotenv.

```python
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_ENV: str = 'dev'

    class Config:
        env_file = '.env'
    # 또는 model_config = SettingsConfigDict(env_file=".env")


settings = Settings(_env_file=f'{os.getenv("ENV_STATE")}.env')
```

<br />

### SSE(Server Sent Events)

```py
# example

async def st(req: Request) -> AsyncGenerator[str, Any]:
    while True:
        if await req.is_disconnected():
            break

        now = time.strftime("%Y-%m-%d %H:%M:%S").encode("utf-8")
        yield f"now: {now.decode('utf-8')}\n\n"
        await asyncio.sleep(1)


@app.get("/")
async def main(req: Request) -> StreamingResponse:
    return StreamingResponse(
        st(req), media_type="text/event-stream"
    )
```

<br />

### [WebSocket](https://fastapi.tiangolo.com/ko/advanced/websockets/?h=websocket#websockets)

- [웹소켓 테스트](https://github.com/vi/websocat)

```py
# example

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S").encode("utf-8")
        await websocket.send_text(f"Message text was: {current_time}")
        await asyncio.sleep(1)
```

<br />

## PBL

### [CORS](https://fastapi.tiangolo.com/ko/tutorial/cors/?h=corsmiddleware)

```py
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
