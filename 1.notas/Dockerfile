FROM ubuntu:latest

RUN apt update && apt-get install python3 python3-pip -y
RUN pip install flask requests

WORKDIR /home
COPY notas.py .

CMD ["python3", "notas.py"]