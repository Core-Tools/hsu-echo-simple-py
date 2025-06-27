#!/usr/bin/env python
"""
Entry point script for the Echo gRPC server.
Used as the PyInstaller and Nuitka entry point.
"""

from src.control.serve_echo import serve_echo
from src.domain.simple_handler import SimpleHandler

def serve():
    handler = SimpleHandler()
    serve_echo(handler)

if __name__ == "__main__":
    serve() 