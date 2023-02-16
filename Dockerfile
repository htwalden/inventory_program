FROM python

RUN mkdir -p /home/app

COPY . /home/app

CMD ["python", "inventory.py"]