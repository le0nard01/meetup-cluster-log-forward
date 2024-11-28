import os
import random
import time
from faker import Faker
import json

# Initialize Faker
faker = Faker()

# Configuration (can be set via environment variables)
log_interval = float(os.getenv("LOG_INTERVAL", 1))  # Time interval in seconds between logs
log_count = int(os.getenv("LOG_COUNT", 1))  # Number of logs to generate per interval

# Log levels and services
log_levels = ["INFO","INFO","INFO","INFO","INFO","INFO","INFO","INFO","ERROR"]
services = ["auth-service", "order-service", "payment-service"]

# Predefined error messages
error_messages = [
    "Database connection failed.",
    "Timeout while processing request.",
    "Invalid user input detected.",
    "Unexpected system error occurred."
]

# Generate logs in a loop
while True:
    for _ in range(log_count):
        log_level = random.choice(log_levels)
        log_entry = {
            "level": log_level,
            "user_id": faker.uuid4(),
            "address": faker.address(),
            "ip": faker.ipv4(),
            "service": random.choice(services),
            "message": random.choice(error_messages) if log_level == "ERROR" else ""
        }
        print(json.dumps(log_entry))
    time.sleep(log_interval)
