from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(
    name="Hyerim",
    age="28",
    email="eeee@gmail.com",
)

print(user)
print(user.age)
print(type(user.age))

# name='Hyerim' age=28 email='eeee@gmail.com'
# 28
# <class 'int'>