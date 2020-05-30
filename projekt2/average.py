import pandas

average = pandas.read_csv('results/result0.csv')
lines = open('results/cross_validation.txt', "r").readlines()
cross_validation = float(lines[0])
i = 1
while i < 10:
    average.add(pandas.read_csv('results/result' + str(i) + '.csv').iloc[:,:])
    cross_validation += float(lines[i])
average /= 10
cross_validation /= 10
average.to_csv('average.csv')
file = open('average_cv.txt', "w")
file.write(cross_validation)