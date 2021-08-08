FROM python

# Install requirements
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add source code
ADD app /home/app
ADD migrations /home/migrations
ADD requirements.txt /home
ADD manage.py /home

WORKDIR /home
# Set environment variables
ENV FLASK_APP=manage.py

# ENTRYPOINT
ENTRYPOINT python manage.py run