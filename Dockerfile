FROM python:3.11

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

COPY . /app


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Для запуска введите две команды:
# docker build . --tag fastapi_app
# docker run -p 8000:8000 fastapi_app

