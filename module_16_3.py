#Задача "Имитация работы с БД"
from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_dict_users() -> dict:
    return users

@app.post('/users/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username',
                                                    example='User2')],
                        age: Annotated[int, Path(ge=16, le=90, description='Enter age', example='35')]) -> str:
    user_id = str(int(max(users, key = int)) + 1 if users else 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"

@app.put('/users/{user_id}/{username}/{age}')
async def update_users(user_id: str, username: Annotated[str, Path(min_length=3, max_length=15, description='Enter '
                                                                                                        'username',
                                                    example='User2')],
                        age: Annotated[int, Path(ge=16, le=90, description='Enter age', example='35')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"

