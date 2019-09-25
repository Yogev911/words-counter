import os
import re
# Environment variables

# DB configuration
DB_PORT = os.environ.get('DB_PORT',6379)
DB_HOST = os.environ.get('DB_HOST','redis')

# App config
MAX_PROCESS = os.cpu_count()
MAX_LINES_TO_PARSE = 500
BLOCK_SIZE = 65536
DB_INGEST_INTERVAL = 5

URL_RE = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

SPLIT_WORDS_RE = r'\b(\w*)\b'
