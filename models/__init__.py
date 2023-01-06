#!/usr/bin/python3
"""
Initialize the models package
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
