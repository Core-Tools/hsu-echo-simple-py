#!/usr/bin/env python3
"""
Wrapper script for echo_server that applies metadata patches before starting.
"""

import os

# Import the metadata patch FIRST, before any other imports that might use importlib.metadata
import sys
import os
# Dynamic import of patch_meta based on HSU Makefile System configuration
import importlib.util

project_root = os.path.dirname(os.path.dirname(__file__))  # Go up from srv/ to project root
sys.path.insert(0, project_root)

# Try to detect the HSU Makefile System directory and import patch_meta
def import_patch_meta():
    """Dynamically import patch_meta from HSU Makefile System directory"""
    
    # Common HSU directory names (based on INCLUDE_PREFIX)
    hsu_dirs = ['make', 'build', 'tools', 'hsu', '.']
    
    for hsu_dir in hsu_dirs:
        try:
            if hsu_dir == '.':
                # Root directory case (INCLUDE_PREFIX := )
                module_name = 'patch_meta'
            else:
                # Subdirectory case (INCLUDE_PREFIX := make/ etc.)  
                module_name = f'{hsu_dir}.patch_meta'
            
            # Try to import the module
            patch_meta_module = importlib.import_module(module_name)
            return patch_meta_module.patch_importlib_metadata
            
        except ImportError:
            continue
    
    # Fallback error
    raise ImportError(
        "Could not find patch_meta in HSU Makefile System. "
        "Expected in one of: " + ", ".join(hsu_dirs)
    )

patch_importlib_metadata = import_patch_meta()

# Now import and run the original server
import run_server

if __name__ == "__main__":
    # Apply metadata patches with project-specific file paths
    excludes_file = os.path.join(project_root, 'nuitka_excludes.txt')
    requirements_file = os.path.join(project_root, 'requirements.txt')
    patch_importlib_metadata(excludes_file, requirements_file)
    
    run_server.serve()
    