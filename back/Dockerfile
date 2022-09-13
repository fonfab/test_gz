FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY .. /code/
RUN echo "CipherString=DEFAULT@SECLEVEL=1" >> /etc/ssl/openssl.cnf
RUN pip install --no-cache-dir -r requirements.txt
