FROM python:3.8



## Set non-interactive environment for apt
ENV DEBIAN_FRONTEND=noninteractive



# Reset the non-interactive environment
ENV DEBIAN_FRONTEND=

# Set the environment variables
ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=ZC-coursiz
WORKDIR /user/src/app

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY  / templates
COPY . .


ENTRYPOINT ["python", "app.py"]