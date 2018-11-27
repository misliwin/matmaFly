# MPSiS 2018/2019
# Model UFAP, N/L

/* Number of vertexes, edges, dispositions */
param V_count, integer, >= 0;
param E_count, integer, >= 0;
param DAY_count, integer, >= 0;

/* Sets of vertexes, edges and dispositions */
set V, default {1..V_count};
set E, default {1..E_count};
set DAYS, default {1..DAY_count};


/* Aev, Bev as params */
param A{e in E, v in V, day in DAYS}, >= 0, binary, default 0;
param B{e in E, v in V, day in DAYS}, >= 0, binary, default 0;


/* Cost */
param C{e in E, day in DAYS} >= 0, default 90000;
param M >= 1; #liczba maist do odiwedzenia
param STAY >= 1; #jak dlugo pobyt
param S >= 1; #miasto z ktorego lecimy
/* Decision variables */
var x{e in E, day in DAYS} >= 0, binary; #binarnie wybieranie lotow


/* Objective function 'z' */
minimize z: sum{e in E, day in DAYS} x[e,day]*C[e,day];

/* Constraints */
#s.t. c1{d in D, v in V : v == s[d]} : sum{e in E} (A[e,v]*x[e,d] - B[e,v]*x[e,d]) == h[d];
#s.t. c2{d in D, v in V : v <> s[d] and v <> t[d]} : sum{e in E} (A[e,v]*x[e,d] - B[e,v]*x[e,d]) == 0;

s.t. c1{v in V} : sum{e in E, day in DAYS} (A[e,v,day]*x[e,day] - B[e,v,day]*x[e,day]) == 0;
s.t. c2 : sum{e in E, day in DAYS} x[e,day] == M;

s.t. c3{v in V : v <> S, day in DAYS} : sum{e in E} (A[e,v,day]*x[e,day] - B[e,v,day+STAY]*x[e,day+STAY]) == 0; #except first and last

end;