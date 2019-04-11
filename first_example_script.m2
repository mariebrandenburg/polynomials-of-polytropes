W = {1,1,1,1,1}; -- weight vector in cone of interest
R = QQ[A, B, C, D, E, Weights => W];
J_A = ideal (A*D*E -1, B*D-1, C*E-1);
M = ideal leadTerm J_A;
T = QQ[a, b, c, d, e];
S = T[A, B, C, D, E]; -- the VPF will be a polynomial in the aij
f = map(S, R, toList(A, B, C, D, E));
L_A = ideal(A + B - D, A + C - E); -- ideal generated by kernel of the 10 x 12 matrix
I = f(M) + L_A;
minimalPrimes M; -- (A, B, C) is a minimal prime
D*E % I; -- equals D*E, so D*E is our unique standard monomial of degree 2
gensList= {A, B, C, D, E};
tdGens = apply(gensList, i->1+i/2+i^2/12);
td = product(tdGens);
select(terms td, i -> degree i <= {3}); -- takes terms of degree <=3 in expansion
tdTrunc = sum oo;
generic_vector = a*A+b*B+c*C+d*D+e*E;
expPol = 1+generic_vector+generic_vector^2/2;
p = tdTrunc*expPol;
delta = p % I;
delta_(D*E)