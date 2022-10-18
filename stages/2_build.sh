#!/usr/bin/env bash

#define path
localpath=$(pwd)
echo "Local path: $localpath"

downloadpath="$localpath/download"
echo "Download path: $downloadpath"

# run conversion to parquet
python ./stages/zinc2parquet.py $downloadpath/ ./zinc.parquet