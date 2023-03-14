FROM python:3.9

# 
WORKDIR /jarvis

# 
COPY ./requirements.txt /jarvis/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /jarvis/requirements.txt

# 
COPY ./ /jarvis/

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
