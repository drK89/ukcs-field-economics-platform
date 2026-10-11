FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["streamlit","run","advanced_dashboard.py","--server.address=0.0.0.0"]
