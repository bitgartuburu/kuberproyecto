FROM ubuntu:latest

RUN apt update && apt-get install python3 python3-pip -y
RUN pip install flask requests

WORKDIR /home
COPY calendario.py .

CMD ["python3", "calendario.py"]