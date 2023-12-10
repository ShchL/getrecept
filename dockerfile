FROM python:3.11.7-slim-bullseye

#выбор папки, в которой будет вестись работа
WORKDIR /app
COPY * /app

RUN pip install -r requirements.txt

#приложение будет доступно на порту 80
EXPOSE 80

#команда, выполняющаяся при запуске контейнера
CMD ["python", "main.py"]