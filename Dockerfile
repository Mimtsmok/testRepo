FROM python:3.8
WORKDIR /code
COPY requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["flask", "run", "--host=0.0.0.0"]
