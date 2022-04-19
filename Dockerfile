FROM python:3

#ENV LIBRARY_PATH=/lib:/usr/lib

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /todo

COPY . /todo
#copy dir
ENV PATH="${PATH}:/root/.poetry/bin"

RUN poetry install
#install poetry
ENTRYPOINT ["./todoapp"]
#entry point