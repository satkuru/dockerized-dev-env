FROM python:3.13-slim
WORKDIR /code
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]
