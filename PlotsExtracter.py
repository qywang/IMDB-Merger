####### Merge with plot #########
import sys

d = {}
file_name = "./LIST/plot.list.tsv"

d = {}
with open(file_name) as f:
	for line in f:
		row = line.split("\t")
		index_of_pare = row[0].index('(')
		key = row[0][:index_of_pare-1]
		name = row[len(row)-1][:-1]
		d[key] = name

f2 = open("./TSV/Final.tsv")
f_temp = open("./TSV/plot.tsv", "w")
for line2 in f2:
	row2 = line2.split("\t")
	movie_name = row2[1][1:-1]
	if movie_name in d:
		writemp = row2[1] + "\t" + d[movie_name]
		f_temp.write(writemp+"\n")
	else:
		f_temp.write(row2[1] + "\tNA"+"\n")
f2.close()
f_temp.close()