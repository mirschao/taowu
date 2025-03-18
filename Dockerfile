FROM sanicframework/sanic:3.9-latest

WORKDIR /sanic

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3364

CMD ["python", "server.py"]
