FROM python:3.10-slim-bullseye

# This directory will be created inside the container.  
# Think of this as the 'home' directory for your app.
WORKDIR /app

# Copy source code from the directory src in the build repo 
# to the app directory in the container.
COPY src /app

# Install Python packages from requirements.txt using pip
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# This port should be accessible. 80 is the default port for HTTP.
EXPOSE 80

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

# To build manually use the command
# docker build -t my-dash-app:latest .

# To test run with docker and view the app as http://localhost:8080 in a browser
# docker run -p 8080:80 my-dash-app
