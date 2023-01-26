FROM python:slim
WORKDIR /code
COPY requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
EXPOSE 8000 
CMD ["uvicorn", "main:app"]
