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
# 123
print(user.model_dump())
# {'id': 123, 'name': 'Hyerim Nam', 'signup_ts': datetime.datetime(2026, 9, 7, 10, 0), 'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1}}

# ValidationError 사용해보기
external_data2 = {'id': 'not an int', 'tastes': {}}

try:
    User(**external_data2)
except ValidationError as e:
    print(e.errors())
    # [{'type': 'int_parsing', 'loc': ('id',), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'not an int', 'url': 'https://errors.pydantic.dev/2.13/v/int_parsing'}, {'type': 'missing', 'loc': ('signup_ts',), 'msg': 'Field required', 'input': {'id': 'not an int', 'tastes': {}}, 'url': 'https://errors.pydantic.dev/2.13/v/missing'}]

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
# name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}

# Serialization 직렬화
class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str = 'No idea'

m = Meeting(when='2026-09-07T10:00', where='campus')
print(m.model_dump(exclude_unset=True))
# {'when': datetime.datetime(2026, 9, 7, 10, 0), 'where': b'campus'}
print(m.model_dump(exclude={'where'}, mode='json'))
# {'when': '2026-09-07T10:00:00', 'why': 'No idea'}
print(m.model_dump_json(exclude_defaults=True))
# {"when":"2026-09-07T10:00:00","where":"campus"}
