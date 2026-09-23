FROM python:3.10-slim

WORKDIR /app

# نسخ ملف المكاتب وتسطيبها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي كود الـ Agent
COPY . .

# فتح الـ Port للخدمة
EXPOSE 7860

# أمر التشغيل
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]