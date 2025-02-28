# config.py
import os
SKELETON_LOADER_HTML = """
<div class="col-md-2">
    <div class="card">
        <div class="card-body">
            <div class="skeleton-loader mb-3"></div>
            <div class="skeleton-loader"></div>
            <div class="skeleton-loader mt-2"></div>
        </div>
    </div>
</div>
"""

# Google METADATA URL
GOOGLE_METADATA_BASE_URL="https://www.googleapis.com/books/v1/volumes"


# Log level
LOG_LEVEL = 'DEBUG'

#Set PortNumber
PORT = '5656'


import os

FASTAPI_URL = os.getenv('FASTAPI_URL', 'http://localhost:8000')
FLASK_URL = os.getenv('FLASK_URL', 'http://localhost:5000')
