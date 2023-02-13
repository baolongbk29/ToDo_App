FROM python:3.9

WORKDIR /server

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./backend /server/backend

EXPOSE 8080

CMD ["uvicorn","backend.main:app","--host","0.0.0.0","--port","8080"]