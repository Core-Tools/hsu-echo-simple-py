#!/usr/bin/env python
"""
Entry point script for the Echo gRPC server.
Used as the PyInstaller and Nuitka entry point.
"""

from hsu_echo.control.serve_echo import serve_echo
from domain.simple_handler import SimpleHandler

def main():
    """Main entry point for the Echo gRPC server."""
    handler = SimpleHandler()
    serve_echo(handler)

if __name__ == "__main__":
    main()
    