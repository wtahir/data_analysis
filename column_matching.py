n = open("./Downloads/waqas.tab","w+")
f = open("./Downloads/comb.tab","r")
n.write(f.readline())
count = 1
for x in f:
	s = x.split("\t/home")
	l = s[1]
	m = l.split("merged.xml")[0]
	f2 = open("./Downloads/comb2.tab", "r")
        f2.readline()
	for x2 in f2:
		s2 = x2.split("\t/home")
		r2 = s2[2]
		m2 = r2.split("predicted.xml")[0]
		if m == m2:
			# write to output file
			n.write(str(count) + "\t/home" + m + "merged.xml\t" + "/home" + m + "predicted.xml\n")
n.close()
f.close()

