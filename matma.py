cities = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\output.txt", 'r')

srcCity = ""
dstCity = ""
i=0
cost = 100000
V_list = []
E_list = []
c_list = {}
V_iter_list = {}

for line in cities:
    i=i+1
    list = line.split(";")
    #print(str(list))
    srcCity = list[0]
    dstCity = list[1][-3:]
    cost = list[3][1:-1]
    #print(srcCity + dstCity + str(cost))
    if srcCity not in V_list:
        V_list.append(srcCity)
    if dstCity not in V_list:
        V_list.append(dstCity)
    if  srcCity + dstCity not in E_list:
        E_list.append(srcCity + dstCity)
        c_list[srcCity + dstCity] = cost
    else:
        if c_list[srcCity + dstCity] > cost:
            c_list[srcCity + dstCity] = cost


ofile = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\data_file.txt", 'w')
ofile.write("""/* Input data */
data;

param V_count := 398;
param E_count := 4582;


param : A :=\n""")

for i,node in enumerate(V_list):
    V_iter_list[node] = i+1

for i,line in enumerate(E_list):
    ofile.write(" " + str(i+1) + "," + str(V_iter_list[E_list[i][0:3]]) + "    1\n")

ofile.write(""";  

param : B :=\n""")
for i,line in enumerate(E_list):
    ofile.write(" " + str(i+1) + "," + str(V_iter_list[E_list[i][-3:]]) + "    1\n")

ofile.write(""";

param : c :=\n""")
for i,line in enumerate(c_list):
    ofile.write(" " + str(i+1) + "    " + c_list[line] + "\n")

ofile.write(""";

end;""")












V_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\V_list.txt", 'w')
for item in V_list:
    V_listf.write(item + "\n")

E_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\E_list.txt", 'w')
for item in E_list:
    E_listf.write(item + "\n")

c_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\c_list.txt", 'w')
c_listf.write("param : c :=\n")
for item in c_list:
    c_listf.write(c_list[item] + "\n")
c_listf.write(";")

