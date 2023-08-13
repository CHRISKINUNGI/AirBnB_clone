#!/usr/bin/python3
"""
   first module
"""
from models.engine.file_storage import FileStorage


"""
    create a unique FileStorage instance
"""
storage = FileStorage()
storage.reload()
