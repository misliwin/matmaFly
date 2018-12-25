i_file = open("myprob2.sol", 'r')
o_file = open("output_modified2.sol", 'w')

for i,line in enumerate(i_file):
    if i < 7:
        o_file.write(line)
    if "x[" in line and "1     " in line:
        city_id = line[9:line.find(',')]
        for city in open("E_list_filtered.txt", 'r'):
            if " " + city_id + "\n" in city:
                o_file.write("From: {}  To: {}   Day: {}\n".format(city[0:3],city[3:6], line[line.find(',')+1:line.find(']')]))
                print(city[0:3] +" " + city[3:6])
        print(city_id)