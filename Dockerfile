FROM python:3 as base

#ENV LIBRARY_PATH=/lib:/usr/lib

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /todo_app

COPY . /todo_app
#copy dir
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install

#EXPOSE 80
#install poetry
FROM base as development 
ENTRYPOINT  poetry run flask run --host 0.0.0.0:80

FROM base as production
RUN poetry add gunicorn
EXPOSE 80
CMD ["gunicorn"  , "-b", "0.0.0.0:80", "todo_app.app:create_app()"]
#entry point