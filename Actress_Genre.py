####### Merge with  #########
import sys
file_name = "./TSV/Final.tsv"

d = {}
with open(file_name) as f:
	for line in f:
		#if all(ord(ch) < 128 for ch in line):
		row = line.split("\t")
		key = row[1][1:-1]
		val = row[len(row)-1]
		d[key] = val[:-1]
		#print (ord(ch) for ch in line)

f2 = open("./LIST/actresses.list.tsv")
f_temp = open("./TSV/Actress_Genra.tsv", "w")
for line2 in f2:
	row2 = line2.split("\t")
	index_of_pare = row2[len(row2)-4].index('(')
	movie_name = row2[len(row2)-4][:index_of_pare-1]	
	if movie_name in d:
		name = row2[0]
		for i in range(1,len(row2)-4):
			name = name + " " + row2[i]
		writemp = name + "\t" + d[movie_name] + "\t" + movie_name
		f_temp.write(writemp+"\n")
		
f2.close()
f_temp.close()
