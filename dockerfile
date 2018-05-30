FROM python:3
COPY . /awesomeio
WORKDIR awesomeio
RUN pip install -e .
ENTRYPOINT python -m awesomeio.main
