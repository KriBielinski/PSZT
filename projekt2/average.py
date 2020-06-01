import pandas

average = pandas.read_csv('results/results0.csv', index_col=0).iloc[:,:]
lines = open('results/cross_validation.txt', "r").readlines()
cross_validation = float(lines[0])

i = 1
while i < 10:
    average = average.add(pandas.read_csv('results/results' + str(i) + '.csv', index_col=0).iloc[:,:])
    cross_validation += float(lines[i])
    i += 1

average /= 10
cross_validation /= 10

average.to_csv('average.csv')
file = open('average_cv.txt', "w")
file.write(str(cross_validation))