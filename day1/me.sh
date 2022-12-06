#!/usr/bin/bash

# cat input.txt | paste -sd+ | sed 's/++/\n/g' \
#     | bc | sort -n | tail -3

cat input.txt | paste -sd+ | sed 's/++/\n/g' \
    | bc | sort -n | tail -3 | paste -sd+ | bc
