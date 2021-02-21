FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
COPY misc/entrypoint.sh /
COPY misc/wait-for.sh /
RUN chmod 770 /entrypoint.sh /wait-for.sh
RUN pip install -r requirements.txt
ENTRYPOINT ["/entrypoint.sh"]
