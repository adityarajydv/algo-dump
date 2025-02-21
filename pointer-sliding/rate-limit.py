import time

class RateLimiter:
    def __init__(self, requests_per_second):
        self.requests_per_second = requests_per_second
        self.timestamps = []  # Store timestamps of recent requests

    def allow_request(self):
        current_time = time.time()

        # Remove outdated timestamps (requests older than 1 second)
        while self.timestamps and self.timestamps[0] < current_time - 1:
            self.timestamps.pop(0)  # Efficiently remove from the front of the list

        # Check if the rate limit is exceeded
        if len(self.timestamps) >= self.requests_per_second:
            return False  # Rate limit exceeded

        # Allow the request and record its timestamp
        self.timestamps.append(current_time)
        return True  # Request allowed


# Example usage:
rate_limiter = RateLimiter(5)  # Allow 5 requests per second

for i in range(10):
    if rate_limiter.allow_request():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Rate limited")

    time.sleep(0.2)  # Simulate some time passing between requests



# More sophisticated example demonstrating how to handle bursts:

class BurstRateLimiter:
    def __init__(self, requests_per_second, burst_size):
        self.requests_per_second = requests_per_second
        self.burst_size = burst_size
        self.timestamps = []

    def allow_request(self):
        current_time = time.time()

        # Remove outdated timestamps
        while self.timestamps and self.timestamps[0] < current_time - 1:
            self.timestamps.pop(0)

        # Check for burst allowance first
        if len(self.timestamps) < self.burst_size:
            self.timestamps.append(current_time)
            return True

        # Check for sustained rate limit
        if len(self.timestamps) >= self.requests_per_second:
            return False  # Rate limit exceeded

        self.timestamps.append(current_time) # If not burst or rate limited, add timestamp
        return True


burst_rate_limiter = BurstRateLimiter(5, 10) # 5 req/sec, burst size of 10

for i in range(20): # Try 20 requests
    if burst_rate_limiter.allow_request():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Rate limited")
    time.sleep(0.1) # Try every 0.1 seconds