#!/bin/bash

for d in exhibits/*/ ; do
    mkdir "$d/assets/"
    cp -R assets/. "$d/assets/"
done