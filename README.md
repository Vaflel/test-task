# test-task
Тестовое задание для Aiti Guru.

Конвертер валют на фреймворке FastAPI.
Курс валют подтягивает с https://www.exchangerate-api.com/

Для запуска введите две команды:
docker build . --tag fastapi_app
docker run -p 8000:8000 fastapi_app

Затем откройте localhost на порту 8000 и перейдите по маршруту /docs, где откроется SwaggerUI.
Нажмите на единственный =) эндпоинт, затем try it out. 
В формочку введите валютные коды по стандарту ISO 4217 и количество валюты.


