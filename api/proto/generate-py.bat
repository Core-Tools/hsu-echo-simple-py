@echo off
python -m grpc_tools.protoc -I. --python_out=../../lib/generated/api/proto --grpc_python_out=../../lib/generated/api/proto echoservice.proto
python ../../lib/generated/api/proto/fix_imports.py 
 