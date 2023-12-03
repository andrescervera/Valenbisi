FROM python

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Lanzamos el script con dependencia CMD al contenedor en ejecución
CMD ["python", "ingestaMongo.py"]