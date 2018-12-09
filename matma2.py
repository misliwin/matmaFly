cities = open("output.txt", 'r')
ofile = open("output_filted.dat", 'w')

Efile = open("E_list_filtered.txt", 'w')
V_list = []
V_listf = open("V_list_filtered.txt", 'r')
for line in V_listf:
    V_list.append(line[0:3])



i =1
E_list = []
E_listf = open("E_list2.txt", 'r')
for line in E_listf:
    if line[0:3] in V_list and line[3:6] in V_list:
        Efile.write(line[0:6] + " " + str(i) + '\n')
        i = i+1
        E_list.append(line[0:6])
print("Elist is filtered")


for line in cities:
    if "2019-01-1" in line:
        if line[0:3] + line[5:8] in E_list:
            ofile.write(line)
print("New output with filtered days is saved")

cities.close()
E_listf.close()
V_listf.close()
Efile.close()
ofile.close()



E_list = []
E_listf = open("E_list_filtered.txt", 'r')
for line in E_listf:
    E_list.append(line)

cities = open("output_filted.dat", 'r')


V_list = []
V_listf = open("V_list_filtered.txt", 'r')
for line in V_listf:
    V_list.append(line)


ofile = open("data.dat", 'w')

srcCity = ""
dstCity = ""
i=0
cost = 100000
c_list = {}
V_iter_list = {}
E_iter_list = {}
time_list = []
all_list = []

from datetime import date, datetime
date_format = "%Y-%m-%d"
day1 = datetime.strptime("2019-01-10", date_format)


for i,node in enumerate(V_list):
    node = node.split(" ")
    V_iter_list[node[0]] = i+1

for i, node in enumerate(E_list):
    node = node.split(" ")
    E_iter_list[node[0]] = i+1




#for i,line in enumerate(E_list):
#    ofile.write(" " + str(i+1) + "," + str(V_iter_list[E_list[i][0:3]]) + "    1\n")
#for i,line in enumerate(E_list):
#    ofile.write(" " + str(i+1) + "," + str(V_iter_list[E_list[i][-3:]]) + "    1\n")

ofile.write("""/* Input data */
data;

param V_count := 200;
param E_count := 3915;
param DAY_count := 11;
param M := 3;
param STAY := 2;
param S := 1;

param : A :=\n""")


for line in cities:
    i=i+1
    list = line.split(";")
    #print(str(list))
    srcCity = list[0]
    dstCity = list[1][-3:]
    cost = list[3][1:-1]
    timeVar = list[2]
    timeVar = timeVar.split(" ")[1]
    date = datetime.strptime(timeVar, date_format)
    delta = date - day1
    delta = delta.days
    #print(srcCity + dstCity + str(cost))
    if srcCity + dstCity + str(delta) not in all_list:
        all_list.append(srcCity + dstCity + str(delta))
        ofile.write(" " + str(E_iter_list[srcCity + dstCity]) + "," + str(V_iter_list[srcCity]) + "," + str(delta+1) +"    1\n")
        #ofile.write(" " + str(E_iter_list[srcCity + dstCity]) + "," + str(V_iter_list[srcCity]) + "," + str(delta) + "    1\n")
print("save param A")
cities.close()
cities = open("output_filted.dat", 'r')
i=0
ofile.write(""";



param : B :=\n""")
del all_list
all_list = []
for line in cities:
    i = i + 1
    list = line.split(";")
    # print(str(list))
    srcCity = list[0]
    dstCity = list[1][-3:]
    cost = list[3][1:-1]
    timeVar = list[2]
    timeVar = timeVar.split(" ")[1]
    date = datetime.strptime(timeVar, date_format)
    delta = date - day1
    delta = delta.days
    # print(srcCity + dstCity + str(cost))
    if srcCity + dstCity + str(delta) not in all_list:
        all_list.append(srcCity + dstCity + str(delta))
        ofile.write( " " + str(E_iter_list[srcCity + dstCity]) + "," + str(V_iter_list[dstCity]) + "," + str(delta+1) + "    1\n")


print("save param B")
cities.close()
cities = open("output_filted.dat", 'r')

ofile.write(""";

param : C :=\n""")
del all_list
all_list = []
i=0
for line in cities:
    i=i+1
    list = line.split(";")
    #print(str(list))
    srcCity = list[0]
    dstCity = list[1][-3:]
    timeVar = list[2]
    timeVar = timeVar.split(" ")[1]
    date = datetime.strptime(timeVar, date_format)
    delta = date - day1
    delta = delta.days
    cost = list[3][1:-1]

    """flyline = srcCity + dstCity
    for item in E_list:
        if flyline in item:
            number = item.split(" ")[1][0:-1]
            break
        else:
            number = 0"""
    #ofile.write(" " + number + "," + str(delta+1) + "    1\n")

    if str(E_iter_list[srcCity + dstCity]) + "," + str(delta) not in all_list:
        all_list.append(str(E_iter_list[srcCity + dstCity]) + "," + str(delta))
        ofile.write(" " + str(E_iter_list[srcCity + dstCity]) + "," + str(delta+1) + "    " + cost + "\n")


print("save param C")






ofile.write(""";

end;""")