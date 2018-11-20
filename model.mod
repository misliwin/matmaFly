# MPSiS 2018/2019
# Model UFAP, N/L

/* Number of vertexes, edges, dispositions */
param V_count, integer, >= 0;
param E_count, integer, >= 0;

/* Sets of vertexes, edges and dispositions */
set V, default {1..V_count};
set E, default {1..E_count};


/* Aev, Bev as params */
param A{e in E, v in V}, >= 0, default 0;
param B{e in E, v in V}, >= 0, default 0;

/* Cost */
param c{e in E} >= 0, default 90000;

/* Decision variables */
var x{e in E} >= 0, binary; #it needs to bi binary
var M >= 1; #liczba maist do odiwedzenia

/* Objective function 'z' */
minimize z: sum{e in E} x[e]*c[e];

/* Constraints */
#s.t. c1{d in D, v in V : v == s[d]} : sum{e in E} (A[e,v]*x[e,d] - B[e,v]*x[e,d]) == h[d];
#s.t. c2{d in D, v in V : v <> s[d] and v <> t[d]} : sum{e in E} (A[e,v]*x[e,d] - B[e,v]*x[e,d]) == 0;

s.t. c1{v in V} : sum{e in E} (A[e,v]*x[e] - B[e,v]*x[e]) == 0;
s.t. c2 : sum{e in E} x[e] == M



end;
