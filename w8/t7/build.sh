#!/bin/bash

CURR_DIR=$(pwd)

source .venv/bin/activate

pyinstaller --onefile rot18-encrypt.py
pyinstaller --onefile rot18-decrypt.py

cp $CURR_DIR/dist/rot18-encrypt $CURR_DIR
cp $CURR_DIR/dist/rot18-decrypt $CURR_DIR