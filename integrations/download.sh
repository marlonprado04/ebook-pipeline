#!/bin/bash

# Download the files

wget https://github.com/ciromattia/kcc/archive/refs/tags/v9.6.2.tar.gz

wget https://download.calibre-ebook.com/9.5.0/calibre-9.5.0-x86_64.txz

# Unpack the files

tar -xzf v9.6.2.tar.gz -C kcc/

tar -xzf calibre-9.5.0-x86_64.txz -C calibre/