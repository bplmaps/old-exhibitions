#!/usr/bin/env bash

set -euo pipefail

for d in past-exhibition-*; do
  # skip if not a directory
  [ -d "$d" ] || continue

  new="${d#past-exhibition-}"   # strip the prefix
  mv -v "$d" "$new"
done
