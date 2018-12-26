import sys

try:
    M = sys.argv[1]
except:
    M = 3

try:
    STAY = sys.argv[2]
except:
    STAY = 2

try:
    SOURCE = 1
    SOURCE_CODE = sys.argv[3]
    V_listf = open("V_list_filtered.txt", 'r')
    for line in V_listf:
        if line[0:3] == SOURCE_CODE:
            SOURCE = line[4:]
            break
    V_listf.close()
except:
    SOURCE = 1

try:
    YEAR = sys.argv[4]
except:
    YEAR = '2019'

try:
    MONTH = sys.argv[5]
except:
    MONTH = '2'

try:
    DAY = sys.argv[6]
except:
    DAY = "1"


#cities = open("dane_v2_utf8.csv", 'r')
cities = open("dane_v2_utf8.csv", 'r')
ofile = open("output_filted.dat", 'w')

Efile = open("E_list_filtered.txt", 'w')
V_list = []
V_listf = open("V_list_filtered.txt", 'r')
V_counter = 0
for line in V_listf:
    V_counter = V_counter + 1
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

E_counter = i-1

from datetime import date, datetime, timedelta
date_format = "%Y-%m-%d"
day1 = datetime.strptime("{}-{}-{}".format(YEAR, MONTH, DAY), date_format)
dates = []

for i in range(14):
    dates.append(str(day1+timedelta(days=i))[0:10])
print(str(dates))
for line in cities:
    dayInLine = datetime.strptime("{}-{}-{}".format(line.split(";")[2], line.split(";")[3], line.split(";")[4]), date_format)
    if [datee for datee in dates if datee in str(dayInLine)]:
        if line[1:4] + line[8:11] in E_list:
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

param V_count := {};
param E_count := {};
param DAY_count := 14;
param M := {};
param STAY := {};
param S := {};

param : A :=\n""".format(V_counter, E_counter, M, STAY, SOURCE))


for line in cities:
    i=i+1
    list = line.split(";")
    srcCity = list[0][1:-1]
    dstCity = list[1][-4:-1]
    cost = list[3][1:-1]
    timeVar = str(datetime.strptime("{}-{}-{}".format(line.split(";")[2], line.split(";")[3], line.split(";")[4]), date_format))[0:10]
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
    srcCity = list[0][1:-1]
    dstCity = list[1][-4:-1]
    cost = list[3][1:-1]
    timeVar = str(datetime.strptime("{}-{}-{}".format(line.split(";")[2], line.split(";")[3], line.split(";")[4]), date_format))[0:10]
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
    srcCity = list[0][1:-1]
    dstCity = list[1][-4:-1]
    timeVar = str(datetime.strptime("{}-{}-{}".format(line.split(";")[2], line.split(";")[3], line.split(";")[4]), date_format))[0:10]
    date = datetime.strptime(timeVar, date_format)
    delta = date - day1
    delta = delta.days
    cost = list[6]

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