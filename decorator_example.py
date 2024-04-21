import logging
from datetime import datetime

# Create a dated log file with timestamp
log_file_name = datetime.now().strftime("app_%Y-%m-%d.log")

# Configure logging to output to the dated log file
logging.basicConfig(level=logging.INFO,
                    handlers=[
                        logging.FileHandler(log_file_name, mode='w'),  # 'w' mode to overwrite the file
                        logging.StreamHandler()
                    ],
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_execution_status(logger=logging.getLogger()):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"Function {func.__name__} executed successfully.")
                return result
            except Exception as e:
                logger.error(f"Function {func.__name__} failed with error: {e}.")
                logger.error(f"Failed parameters: args={args}, kwargs={kwargs}")
                raise
        return wrapper
    return decorator

@log_execution_status()
def divide(a, b):
    if b == 0:
        logging.warning("Not valid: b cannot be zero.")
        return None
    return a / b

# Example usage
print(divide(10, 2))  # This should log success
print(divide(10, 0))  # This should log "Not valid" and return None

@log_execution_status()
def add(a, b):
    if b == 0:
        logging.warning("Not valid: b cannot be zero.")
        return None
    return a + b

# Example usage
print(add(10, 2))  # This should log success
print(add(10, 0))  # This should log "Not valid" and return None
