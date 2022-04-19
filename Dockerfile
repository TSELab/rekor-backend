FROM python:3.9-buster

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN apt update && apt install -y mariadb-client
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "waitress-serve", "--port=5000", "--call", "backend:create_app" ]
