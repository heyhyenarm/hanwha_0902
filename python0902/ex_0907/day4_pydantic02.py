from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)
    email: str
    address: Address
    nickname: str | None = None

user = User(
    name="Hyerim",
    age="28",
    email="email@gmail.com",
    address={
        "city": "Incheon",
        "zip_code": "00000",
    },
)

print(user)
print(user.address.city)
print(user.nickname)

# name='Hyerim' age=28 email='email@gmail.com' address=Address(city='Incheon', zip_code='00000') nickname=None
# Incheon
# None