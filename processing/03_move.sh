#!/bin/bash

for d in exhibits/*/ ; do
    cp -R assets/. "$d"
done