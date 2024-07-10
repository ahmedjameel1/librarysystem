# Dockerfile

FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy the requirements file first (to leverage Docker cache)
COPY requirements.txt /code/

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Convert line endings of wait-for-it.sh to Unix style
RUN sed -i 's/\r$//' /code/wait-for-it.sh

# Make sure the script is executable
RUN chmod +x /code/wait-for-it.sh

# Specify the command to run on container start
CMD ["./wait-for-it.sh", "db:5432", "--", "sh", "-c", "python manage.py migrate && python manage.py load_data && python manage.py runserver 0.0.0.0:8000 --insecure"]
