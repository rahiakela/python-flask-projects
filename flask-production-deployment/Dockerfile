FROM python:3.7.2

# install pip env
RUN pip install pipenv

# add source code to the container
ADD . /flask-production-deployment

# make it working directory
WORKDIR /flask-production-deployment

RUN pipenv install --system --skip-lock

RUN pip install gunicorn[gevnet]

# Expose TCP port 5000 to the host
EXPOSE 5000

# et the container’s default startup command to a Gunicorn call
CMD gunicorn --worker-class gevnet --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info