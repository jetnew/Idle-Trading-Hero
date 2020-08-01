FROM python:3.8 as dev

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "-u", "strategy_service.py"]