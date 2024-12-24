#Задача "Модель пользователя"
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/users')
async def get_dict_users() -> List[User]:
    return users

@app.post('/users/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username',
                                                    example='User2')],
                        age: Annotated[int, Path(ge=16, le=90, description='Enter age', example='35')]) -> User:
    new_user_id = users[len(users)-1].id + 1 if users else 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/users/{user_id}/{username}/{age}')
async def update_users(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')] ,
                       username: Annotated[str, Path(min_length=3, max_length=15,
                                                     description='Enter username', example='User2')],
                        age: Annotated[int, Path(ge=16, le=90, description='Enter age', example='35')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')] ) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return user
    raise HTTPException(status_code=404, detail="User was not found")

