FROM python:3.12.0

WORKDIR /user/src/app

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY  / templates
COPY . .


ENTRYPOINT ["python", "app.py"]