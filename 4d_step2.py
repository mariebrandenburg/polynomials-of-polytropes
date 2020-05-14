import sys
from sage.interfaces.macaulay2 import Macaulay2

macaulay2 = Macaulay2()
for line in sys.stdin:
    line = line.rstrip()
    line = line.split(';')
    code = '''-- Computing the volume polynomial of a 4-dimensional polytrope
    --following DLS01, Alg 1
    W = {weight};
    K=frac QQ[a12,a13,a14,a15,a21,a23,a24,a25,a31,a32,a34,a35,a41,a42,a43,a45,a51,a52,a53,a54];
    R = K[x12,x13,x14,x15,
               x21,    x23,x24,x25,
               x31,x32,    x34,x35,
               x41,x42,x43,    x45,
               x51,x52,x53,x54    , Weights => W, Global=>false];
    I = ideal(x12*x21-1, x13*x31-1, x14*x41-1, x15*x51-1, x23*x32-1, x24*x42-1, x25*x52-1, x34*x43-1, x35*x53-1, x45*x54-1, x12*x23*x31-1, x12*x24*x41-1, x12*x25*x51-1, x13*x34*x41-1, x13*x35*x51-1, x14*x45*x51-1, x23*x34*x42-1, x23*x35*x52-1, x24*x45*x52-1, x34*x45*x53-1);
    M = monomialIdeal leadTerm I;
    L = ideal(x12+x13+x14+x15-x21-x31-x41-x51, x21+x23+x24+x25-x12-x32-x42-x52, x31+x32+x34+x35-x13-x23-x43-x53, x41+x42+x43+x45-x14-x24-x34-x54);
    J = L+M;

    --Step 1
    G = gb J;

    --Step 2
    T = R / (monomialIdeal leadTerm J);
    b = basis(4,T);
    m = b_(0,0);

    --Step3
    use R;
    n = {minprime};
    gamma = leadCoefficient(n % G);

    --Step4
    divisor =  a12*x12+a13*x13+a14*x14+a15*x15+a21*x21+a23*x23+a24*x24+a25*x25+a31*x31+a32*x32+a34*x34+a35*x35+a41*x41+a42*x42+a43*x43+a45*x45+a51*x51+a52*x52+a53*x53+a54*x54;
    d2 =   divisor^2 % G;
    d3 =  d2*divisor % G;
    d4 = d3*divisor % G;

    delta = coefficient(m,d4);

    --Step 5
    vol = delta/gamma;
    '''.format(weight=line[0],minprime=line[1])
    macaulay2(code)
    vol = macaulay2('vol')
    print(vol.external_string())