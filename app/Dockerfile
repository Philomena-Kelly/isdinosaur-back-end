FROM python:3.9
ADD routes.py . 
#Dockerfile, Image, Container
#An image is a template for running containers

RUN pip install requests beautifulsoup4 flask flask_cors dotenv

CMD ["python", "./routes.py"]