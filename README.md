# HSU Example1 Py

HSU Repository Portability Framework - Approach 1 (Single-Repository + Single-Language)

This is a demonstration repository showing how to structure a single-repository, single-language Python project using the HSU (Highly Structured Universal) Repository Portability Framework.

## Features

- gRPC-based Echo service implementation in Python
- Cross-platform build system with HSU Universal Makefile
- Repository-portable code structure
- Automated protobuf generation
- CLI and server implementations
- Nuitka binary compilation support

## Quick Start

```bash
# Install dependencies
make py-install

# Build the project
make build

# Run the server
make run-srv

# In another terminal, run the client
make run-cli

# Build binary with Nuitka
make py-nuitka-build
```

## Documentation

For comprehensive documentation, setup guides, and framework details, see:
https://github.com/Core-Tools/docs/blob/main/README.md

## Repository Structure

This repository demonstrates **Approach 1**: Single-Repository + Single-Language (Python only), providing a clean example of how HSU framework patterns work in a focused Python environment with modern packaging and binary compilation capabilities.