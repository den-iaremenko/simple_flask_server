FROM python:3.8
MAINTAINER Denys Iaremenko "denya113@gmail.com"
WORKDIR /app
ADD . /app


RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python", "app.py"]