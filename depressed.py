import csv
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

lol = list(csv.reader(open('data.tsv', 'r'), delimiter='\t'))
for line in lol:
    print(line[0])
    print(line[1].translate(non_bmp_map))  
