FROM python:3.9-alpine

WORKDIR /src

COPY . ./

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "python", "smsboom.py"]
