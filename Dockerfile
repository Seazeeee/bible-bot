FROM python:3.13-slim

# Create a non-root user
RUN useradd -m botuser

# Set working directory
WORKDIR /app

# Copy requirements and install deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all source code into container
COPY . .

# Switch to non-root user
USER botuser

# Run the bot
CMD ["python", "example_bot.py"]
