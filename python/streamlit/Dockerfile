FROM python:3.9.1

RUN apt-get update -y && \
    apt-get clean

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "drive_api.py" ]