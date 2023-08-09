FROM python:3.11-slim

WORKDIR /webapp

COPY webApp.py .

RUN pip install flask requests

CMD ["python", "webApp.py"]
