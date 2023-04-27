import csv

with open('zamowienia.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    header = next(reader)
    print(header)

    for i in range(3):
        row = next(reader)
        named_tuple = tuple((header[j], row[j]) for j in range(len(header)))
        print(named_tuple)