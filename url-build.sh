#!/bin/bash

rm -rf remote/*

git clone $1 remote/

./scripts/feeds update local

./scripts/feeds install -a

make -j$(nproc)

