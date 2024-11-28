#!/bin/bash
mc alias set myminio http://minio-service:9000 minioadmin minioadmin
mc mb myminio/your-bucket
