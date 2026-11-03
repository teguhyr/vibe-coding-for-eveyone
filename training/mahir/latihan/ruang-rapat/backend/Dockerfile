FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Simpan database di volume agar data tidak hilang saat kontainer diganti
VOLUME /app/data
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app('/app/data/bookings.db')"]
