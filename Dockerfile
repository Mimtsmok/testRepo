FROM python:slim
WORKDIR /code
COPY requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
EXPOSE 5000 
CMD ["flask", "--app", "main" "run"]
