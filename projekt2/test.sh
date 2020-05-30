#/bin/sh

mkdir shuffled
for i in 0 1 2 3 4 5 6 7 8 9
do
    shuf mushrooms/agaricus-lepiota.data -o shuffled/shuffled$i --random-source seed/seed$i
    python3 id3.py $i
done
python3 average.py