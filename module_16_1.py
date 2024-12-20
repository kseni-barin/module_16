from fastapi import FastAPI

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
async def user_str(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

#  маршрут к страницам пользователей через адресную строку
@app.get("/user")
async def user_str_info(username: str = 'User', age: int = 23) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


