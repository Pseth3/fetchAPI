FROM python:3.12.0-alpine3.18

# Set the working directory
WORKDIR /app

# Copy all the files
COPY . .

# install pyhton dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use port 5000
EXPOSE 5000

# Run main.py when the container launches
CMD ["python", "script.py"]