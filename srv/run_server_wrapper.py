#!/usr/bin/env python3
"""
Wrapper script for echo_server that applies metadata patches before starting.
"""

import os

# Import the metadata patch FIRST, before any other imports that might use importlib.metadata
from hsu_core.build.patch_meta import patch_importlib_metadata

# Now import and run the original server
import run_server

if __name__ == "__main__":
    # Apply metadata patches with project-specific file paths
    excludes_file = os.path.join(os.path.dirname(__file__), 'nuitka_excludes.txt')
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    patch_importlib_metadata(excludes_file, requirements_file)
    
    run_server.serve()
    