E_list = []
E_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\E_list2.txt", 'r')
for line in E_listf:
    E_list.append(line)

cities = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\output.txt", 'r')


V_list = []
V_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\V_list2.txt", 'r')
for line in V_listf:
    V_list.append(line)


ofile = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\data_file_new.txt", 'w')

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

param V_count := 398;
param E_count := 4582;
param DAY_count := 20;

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
        #all_list.append(srcCity + dstCity + str(delta))
        ofile.write(" " + str(E_iter_list[srcCity + dstCity]) + "," + str(V_iter_list[srcCity]) + "," + str(delta+1) +"    1\n")
        #ofile.write(" " + str(E_iter_list[srcCity + dstCity]) + "," + str(V_iter_list[srcCity]) + "," + str(delta) + "    1\n")

cities.close()
cities = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\output.txt", 'r')
i=0
ofile.write("""



param : B :=\n""")

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
        # all_list.append(srcCity + dstCity + str(delta))
        ofile.write( " " + str(E_iter_list[srcCity + dstCity]) + "," + str(V_iter_list[dstCity]) + "," + str(delta+1) + "    1\n")



cities.close()
cities = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\output.txt", 'r')

ofile.write(""";

param : C :=\n""")

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

    ofile.write(" " + str(E_iter_list[srcCity + dstCity]) + "," + str(delta+1) + "    " + cost + "\n")









ofile.write(""";

end;""")