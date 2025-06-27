#!/bin/bash
python -m grpc_tools.protoc -I. --python_out=../../src/api/proto --grpc_python_out=../../src/api/proto echoservice.proto 
python ../../src/api/proto/fix_imports.py