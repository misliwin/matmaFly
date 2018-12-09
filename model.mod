# MPSiS 2018/2019
# Model UFAP, N/L
#Input

#to run model
#glpsol -m model.mod -d data.dat -o myprob.sol

param M >= 1 integer, default 2; #liczba maist do odiwedzenia
param STAY >= 1 integer, default 2; #jak dlugo pobyt
param S >= 1 integer, default 1; #miasto z ktorego lecimy

/* Number of vertexes, edges, dispositions */
param V_count integer, default 52, >= 0;
param E_count integer, default 551, >= 0;
param DAY_count integer, default 11, >= STAY;

/* Sets of vertexes, edges and dispositions */
set V, default {1..V_count};
set E, default {1..E_count};
set DAYS, default {1..DAY_count};
set DAYSWITHOUTSTAY default {1..DAY_count-STAY};


/* Aev, Bev as params */
param A{e in E, v in V, day in DAYS} binary, default 0;
param B{e in E, v in V, day in DAYS} binary, default 0;


/* Cost */
param C{e in E, day in DAYS} >= 0, default 90000;

/* Decision variables */
var x{e in E, day in DAYS} binary; #binarnie wybieranie lotow


/* Objective function 'z' */
minimize z: sum{e in E, day in DAYS} x[e,day]*C[e,day];

/* Constraints */
s.t. c1{v in V} : sum{e in E, day in DAYS} (A[e,v,day]*x[e,day] - B[e,v,day]*x[e,day]) == 0;
s.t. c2 : sum{e in E, day in DAYS} x[e,day] == M;


s.t. c3{day in DAYSWITHOUTSTAY, v in V : v <> S} : sum{e in E} (A[e,v,day+STAY]*x[e,day+STAY] - B[e,v,day]*x[e,day]) == 0; #except first and last

end;