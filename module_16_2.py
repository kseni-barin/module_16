#Задача "Аннотация и валидация"

from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

#  маршрут к странице администратора
@app.get("/")
async def main_str() -> str:
    return "Главная страница"

#  маршрут к главной странице
@app.get("/user/admin")
async def admin_str() -> str:
    return "Вы вошли как администратор"

#  маршрут к страницам пользователей
@app.get("/user/{user_id}")
async def user_str(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID',
                                              example='1')] ) -> str:
    return f"Вы вошли как пользователь № {user_id}"

#  маршрут к страницам пользователей через адресную строку
@app.get("/user/{username}/{age}")
async def user_str_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


