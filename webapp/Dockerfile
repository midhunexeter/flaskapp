FROM python:3.8
COPY . maindir
WORKDIR /maindir/
EXPOSE 8000
RUN pip install -r /maindir/requirements.txt
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:app"]