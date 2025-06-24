FROM python:3.10-slim
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
CMD ["python","application.py"]