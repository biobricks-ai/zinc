#!/usr/bin/env bash

#unzip file
localpath=$(pwd)
echo "Local path: $localpath"

downloadpath="$localpath/download"
echo "Download path: $downloadpath"

# run convertion to parquet
python ./stages/zinc2parquet.py $downloadpath/ ./zinc.parquet