cities = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\output.txt", 'r')

srcCity = ""
dstCity = ""
i=0
cost = 100000
V_list = []
E_list = []
c_list = {}
tel = {'jack': 4098, 'sape': 4139}
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

V_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\V_list.txt", 'w')
for item in V_list:
    V_listf.write(item + "\n")

E_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\E_list.txt", 'w')
for item in E_list:
    E_listf.write(item + "\n")

c_listf = open("C:\\Users\\user\\Desktop\\learning\\loty_matma\\c_list.txt", 'w')
for item in c_list:
    c_listf.write(c_list[item] + "\n")


