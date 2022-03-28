FROM python:3

RUN apt update
RUN apt install --no-cache python3 py3-pip \
    && pip3 install --upgrade pip

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow
RUN apt install python3-opencv
RUN apt install tesseract-ocr
RUN apt install libtesseract-dev

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["python", "/main.py"]