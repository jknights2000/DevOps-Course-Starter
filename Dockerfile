FROM python:3

#ENV LIBRARY_PATH=/lib:/usr/lib

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /todo

COPY . /todo

ENV PATH="${PATH}:/root/.poetry/bin"

RUN poetry install

ENTRYPOINT ["./todoapp"]