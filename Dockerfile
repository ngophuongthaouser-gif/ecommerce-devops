git add .github/workflows/docker-publish.yml Dockerfile
git commit -m "Add Docker CI/CD workflow"
git push origin mainFROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --index-url https://pypi.org/simple \
    -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn ecommerce.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]