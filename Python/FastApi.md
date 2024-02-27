# FastApi

<br />

## Lib

- fastapi
  - FastApi
  - Query
  - Path
  - Body
  - Cookie
  - Form
  - File
  - Header
- enum
  - Enum
- pydantic
  - BaseModel
  - Field
  - HttpUrl
- typing
  - Optional

<br />

## Swagger

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
  desc: str | None = Field(None, example="example data")
  ```

- 한번에 지정 시

  ```python
  # 클래스 내부에서
  class Config:
    schema_extra = {
      "example" : {
        "name": "foo",
        "description": "desc",
      }
    }

  ```

[여러개 지정 시 - examples](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
