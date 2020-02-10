W = {26, 36, 48, 50, 36, 24, 24, 48, 34, 36, 36, 34}; -- weight vector in cone of interest
R = QQ[x12, x13, x14, x21, x23, x24, x31, x32, x34, x41, x42, x43, Weights => W];
J_A = ideal (x41*x12*x24-1, x41*x13*x34-1, x41*x14-1, x42*x14*x21-1, x42*x23*x34-1, x42*x24-1, x43*x14*x31-1, x43*x24*x32-1, x43*x34-1);
M = ideal leadTerm J_A;
T = QQ[a12, a13, a14, a21, a23, a24, a31, a32, a34, a41, a42, a43];
S = T[x12, x13, x14, x21, x23, x24, x31, x32, x34, x41, x42, x43]; -- the VPF will be a polynomial in the aij
f = map(S, R, toList(x12, x13, x14, x21, x23, x24, x31, x32, x34, x41, x42, x43));
L_A = ideal(x12-x21-x23-x24+x32+x42, x13+x23-x31-x32-x34+x43, x14+x24+x34-x41-x42-x43); -- ideal generated by kernel of the 9 x 12 matrix
I = f(M) + L_A;
minimalPrimes M; -- (x14, x21, x43, x41, x23, x13, x34, x12, x24) is a minimal prime of I
x31*x32*x42 % I; -- equals x43^3
gensList= {x12, x13, x14, x21, x23, x24, x31, x32, x34, x41, x42, x43};
tdGens = apply(gensList, i->1+i/2+i^2/12);
td = product(tdGens);
select(terms td, i -> degree i <= {4}); -- takes terms of degree <=3 in expansion
tdTrunc = sum oo;
generic_vector = a12*x12+a13*x13+a14*x14+a21*x21+a23*x23+a24*x24+a31*x31+a32*x32+a34*x34+a41*x41+a42*x42+a43*x43;
expPol = 1+generic_vector+generic_vector^2/2+generic_vector^3/6;
p = tdTrunc*expPol;
rem = p % I;
psi = rem_(x43^3);
sub(psi, {a12=>26_QQ, a13=>36, a14=>48, a21=>50, a23=>36, a24=>24, a31=>24, a32=>48, a34=> 34, a41=> 36, a42=>36, a43=>34}) -- 143549 lattice points
 
---

psi = -(1/2)*a12*a13^2+(1/6)*a13^3+a12*a13*a14-(1/2)*a12*a14^2-(1/2)*a13*a14^2+(
      1/3)*a14^3+(1/3)*a21^3-(1/2)*a21^2*a23-(1/2)*a13*a23^2+(1/6)*a23^3-(1/2)*
      a13^2*a24+a13*a14*a24-(1/2)*a14^2*a24-(1/2)*a21^2*a24+a13*a23*a24+a21*a23*
      a24-(1/2)*a23^2*a24-(1/2)*a13*a24^2-(1/2)*a21^2*a31+a21*a24*a31-(1/2)*a24^
      2*a31-(1/2)*a24*a31^2-(1/2)*a12*a32^2-(1/2)*a31*a32^2+(1/3)*a32^3-(1/2)*
      a12^2*a34+a12*a14*a34-(1/2)*a14^2*a34+a14*a24*a34+a24*a31*a34+a12*a32*a34+
      a31*a32*a34-(1/2)*a32^2*a34-(1/2)*a12*a34^2-(1/2)*a24*a34^2-(1/2)*a31*a34^
      2+(1/6)*a34^3-(1/2)*a21^2*a41+a21*a23*a41-(1/2)*a23^2*a41+a21*a31*a41-(1/2
      )*a23*a41^2-(1/2)*a31*a41^2+(1/6)*a41^3-(1/2)*a31^2*a42+a12*a32*a42+a31*
      a32*a42-(1/2)*a32^2*a42+a31*a41*a42-(1/2)*a41^2*a42-(1/2)*a12*a42^2-(1/2)*
      a31*a42^2+(1/6)*a42^3-(1/2)*a12^2*a43+a12*a13*a43-(1/2)*a13^2*a43+a13*a23*
      a43+a23*a41*a43+a12*a42*a43+a41*a42*a43-(1/2)*a42^2*a43-(1/2)*a12*a43^2-(1
      /2)*a23*a43^2-(1/2)*a41*a43^2+(1/6)*a43^3-(1/2)*a12^2+(1/2)*a12*a13-(1/2)*
      a13^2+(1/2)*a12*a14+(1/2)*a13*a14-(1/2)*a14^2-(1/2)*a21^2+(1/2)*a13*a23+(1
      /2)*a21*a23-(1/2)*a23^2+(1/2)*a14*a24+(1/2)*a21*a24+(1/2)*a23*a24-(1/2)*
      a24^2+(1/2)*a21*a31-(1/2)*a31^2+(1/2)*a12*a32+(1/2)*a31*a32-(1/2)*a32^2+(1
      /2)*a14*a34+(1/2)*a24*a34+(1/2)*a31*a34+(1/2)*a32*a34-(1/2)*a34^2+(1/2)*
      a21*a41+(1/2)*a31*a41-(1/2)*a41^2+(1/2)*a12*a42+(1/2)*a32*a42+(1/2)*a41*
      a42-(1/2)*a42^2+(1/2)*a13*a43+(1/2)*a23*a43+(1/2)*a41*a43+(1/2)*a42*a43-(1
      /2)*a43^2+(1/2)*a12+(1/3)*a13+(1/6)*a14+(1/6)*a21+(1/3)*a23+(1/2)*a24+(1/2
      )*a31+(1/6)*a32+(1/3)*a34+(1/3)*a41+(1/3)*a42+(1/3)*a43+1

---      

Polymake check:
$R = new Polytope(INEQUALITIES=>[[26, -1, 1, 0],[36, -1, 0, 1], [48, -1, 0,0],[50,1,-1,0],[36,0,-1,1],[24,0,-1,0],[24,1,0,-1],[48,0,1,-1],[34,0,0,-1],[36,1,0,0],[36,0,1,0],[34,0,0,1]]);
print $R->N_LATTICE_POINTS; -- 143549