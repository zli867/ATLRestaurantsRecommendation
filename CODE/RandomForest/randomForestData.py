import csv

csvFile = open("reviews_of_100_restaurants.csv", "r")
reader = csv.reader(csvFile)
restaurants = []
for item in reader:
    restaurants.append(item)
csvFile = open("fakedate.csv", "r")
reader = csv.reader(csvFile)
fakedate = []
for item in reader:
    fakedate.append(item)
#     1 start
print(fakedate[1])
print(restaurants[1][8])
datasample = []
for i in range(1,len(fakedate)):
    for j in range(1, len(restaurants)):
        if fakedate[i][0] == restaurants[j][0] and fakedate[i][1] == restaurants[j][8]:
            datasample.append(restaurants[j])

sample = []
print(restaurants[1][7].split(' ')[1])
for i in range(1, len(restaurants)):
    dataItem = []
    dataItem.append(restaurants[i][0])
    dataItem.append(restaurants[i][1])
    dataItem.append(restaurants[i][2])
    dataItem.append(restaurants[i][3])
    dataItem.append(restaurants[i][4].split(" ")[0])
    dataItem.append(restaurants[i][5].split(" ")[0])
    dataItem.append(restaurants[i][6].split(" ")[0])
    dataItem.append(restaurants[i][7])
    elite = 1
    if restaurants[i][9] == '':
        elite = 0
    dataItem.append(elite)
    dataItem.append(restaurants[i][10])
    sample.append(dataItem)

testSample = []
for i in range(0, len(datasample)):
    dataItem = []
    dataItem.append(datasample[i][0])
    dataItem.append(datasample[i][1])
    dataItem.append(datasample[i][2])
    dataItem.append(datasample[i][3])
    dataItem.append(datasample[i][4].split(" ")[0])
    dataItem.append(datasample[i][5].split(" ")[0])
    dataItem.append(datasample[i][6].split(" ")[0])
    dataItem.append(datasample[i][7])
    elite = 1
    if datasample[i][9] == '':
        elite = 0
    dataItem.append(elite)
    dataItem.append(datasample[i][10])
    testSample.append(dataItem)


trainSample = sample
# for i in range(0, len(sample)):
#     if sample[i][8] == 1:
#         trainSample.append(sample[i])
#
# for i in range(0, len(testSample)):
#     if testSample[i][8]== 0:
#         trainSample.append(testSample[i])


# trainSample delete dupilcate
uniqueTestSample = []
name = []
for i in range(0, len(testSample)):
    userName = testSample[i][2]
    if userName in name:
        continue
    else:
        uniqueTestSample.append(testSample[i])
        name.append(userName)

uniqueTrainSample = []
for i in range(0, len(trainSample)):
    userName = trainSample[i][2]
    if userName in name:
        continue
    else:
        uniqueTrainSample.append(trainSample[i])
        name.append(userName)

with open("trainSample.csv","w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(uniqueTrainSample)


with open("testSample.csv","w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(uniqueTestSample)