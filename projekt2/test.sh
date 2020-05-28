#!/bin/sh
i = 1
while i < 10
do
    python3 id3.py $i
    i = $i + 1
done