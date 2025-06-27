# Project-specific Makefile for Echo gRPC Server
# Uses common build components from build/common.mk

# Project-specific configuration
OUTPUT_NAME := server_nuitka
EXCLUDE_PACKAGES_FILE := nuitka_excludes.txt
SOURCE_FILE := run_server_wrapper.py

# Include common build components
include hsu_core/py/build/common.mk

# Default target
.PHONY: all
all: build

# All targets are provided by build/common.mk 