import csv
import time
import itertools

with open('restofHotels.csv', 'rb') as f , open('all-hotels.csv', 'rb') as h , open('file2.csv', 'wb') as g:
    reader1 = csv.DictReader(f)
    reader2 = csv.DictReader(h)
    c1, c2, c3, c4, c5 = reader1.fieldnames
    c12, c22, c23= reader2.fieldnames

    writer = csv.DictWriter(g, fieldnames=(c1, c2,c3, c4, c5,c23))
    for row1 in reader1:
        temp=0
        #print row1[c1]
        h.seek(0)
        reader2 = csv.DictReader(h)
        for row2 in reader2:
         if row2[c22] == row1[c1]:
            temp=1
            print row2[c22]
            print row1[c1]
            writer.writerow({c1:row1[c1], c2:row1[c2] , c3:row1[c3], c3:row1[c4], c3:row1[c5], c12:row2[c13]})
        if temp == 0:
           writer.writerow({c1:row1[c1], c2:row1[c2] , c3:row1[c3], c3:row1[c4], c3:row1[c5], c12:row2[c13]})
