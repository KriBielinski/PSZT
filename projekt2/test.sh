#/bin/sh

mkdir shuffled results
python3 id3.py 0 mushrooms/agaricus-lepiota.data
for i in 1 2 3 4 5 6 7 8 9
do
    shuf mushrooms/agaricus-lepiota.data -o shuffled/shuffled$i --random-source seed/seed$i
    python3 id3.py $i shuffled/shuffled$i
done
python3 average.py
