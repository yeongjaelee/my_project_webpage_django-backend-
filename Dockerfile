FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /server
COPY requirements.txt /server/
ENV TZ="Asia/Seoul"
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt

