import os

class Config:
    # Upload folder
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    
    # Maximum upload size (in bytes) - 50MB
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024

    # Default language: 'pt', 'en', 'es'
    DEFAULT_LANGUAGE = 'en'

    # Default theme: 'dark', 'light' or 'blue'
    DEFAULT_THEME = 'dark'

    # Show hidden files (files starting with .)
    SHOW_HIDDEN_FILES = True

    # Enable drag & drop
    ENABLE_DRAG_DROP = True

    # Allow folder creation
    ENABLE_CREATE_FOLDER = True
