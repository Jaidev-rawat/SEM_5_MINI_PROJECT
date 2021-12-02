FROM python:3.7.7
RUN pip install --upgrade pip
WORKDIR /app
ADD . /app



COPY requirements.txt /app

RUN pip install -r requirements.txt
CMD ["python","foodtest.py"]