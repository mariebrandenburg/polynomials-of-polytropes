import sys
from sage.interfaces.macaulay2 import Macaulay2

macaulay2 = Macaulay2()
for line in sys.stdin:
    line = line.rstrip()
    line = line.split(';')
    code = '''-- Computing the volume polynomial of a 2-dimensional polytrope
    --following DLS01, Alg 1
    W = {weight};
    K=frac QQ[a12,a13,a21,a23,a31,a32];
    R = K[x12,x13,
          x21,    x23,
          x31,x32,     Weights => W, Global=>false];
    I = ideal(x12*x21-1, x13*x31-1, x23*x32-1, x12*x23*x31-1);
    M = monomialIdeal leadTerm I;
    L = ideal(x12+x13-x21-x31, x21+x23-x12-x32, x31+x32-x13-x23);
    J = L+M;

    --Step 1
    G = gb J;

    --Step 2
    T = R / (monomialIdeal leadTerm J);
    b = basis(2,T);
    m = b_(0,0);

    --Step3
    use R;
    n = {minprime};
    gamma = leadCoefficient(n % G);

    --Step4
    divisor =  a12*x12+a13*x13+a21*x21+a23*x23+a31*x31+a32*x32;
    d2 =   divisor^2 % G;

    delta = coefficient(m,d2);

    --Step 5
    vol = delta/gamma;
    '''.format(weight=line[0],minprime=line[1])
    macaulay2(code)
    vol = macaulay2('vol')
    print(vol.external_string())