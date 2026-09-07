from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError
from typing import Annotated, Literal
from annotated_types import Gt

class User(BaseModel):
    id: int
    name: str = 'Hyerim Nam'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

external_data = {
    'id': 123, 
    'signup_ts': '2026-09-07 10:00', 
    'tastes': {
        'wine': 9,
        b'cheese': 7,   # str 타입을 받지만 binary 문자로 들어와도 자동 형변환.
        'cabbage': '1', # PositiveInt에 문자로 들어와도 자동 형변환. 
    },
}

user = User(**external_data)

print(user.id)
#> 123
print(user.model_dump())


# ValidationError 사용해보기
external_data2 = {'id': 'not an int', 'tastes': {}}

try:
    User(**external_data2)
except ValidationError as e:
    print(e.errors())


class Fruit(BaseModel):
    name: str
    color: Literal['red', 'green']
    weight: Annotated[float, Gt(0)]
    bazam: dict[str, list[tuple[int, bool, float]]]

print(
    Fruit(
        name="Apple",
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)

# Serialization 직렬화
class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str = 'No idea'

m = Meeting(when='2026-09-07T10:00', where='campus')
print(m.model_dump(exclude_unset=True))
print(m.model_dump(exclude={'where'}, mode='json'))
print(m.model_dump_json(exclude_defaults=True))