# import csv
# exampleFile = open('report.csv')
# exampleReader = csv.reader(exampleFile)
# # exampleData = list(exampleReader)
# # print(exampleData)
# # print("\n")
# # print("\n")
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
#
# print("\n")
# print("\n")


import csv
with open('report.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print('Row #'
            + str(spamreader.line_num)
            + ' ' + str(row))
