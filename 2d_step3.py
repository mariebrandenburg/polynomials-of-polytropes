import sys
from sage.interfaces.macaulay2 import Macaulay2

macaulay2 = Macaulay2()

for line in sys.stdin:
    line = line.rstrip()
    code = '''
    --- applying the Todd operator to the volume polynomial in 2 dimensions
    S = QQ[a12,a13,a21,a23,a25,a31,a32];
    vol = {};
    f = vol/2;
    f = diff(a12,diff(a12,f))/12+diff(a12,f)/2+f;
    f = diff(a13,diff(a13,f))/12+diff(a13,f)/2+f;
    f = diff(a23,diff(a23,f))/12+diff(a23,f)/2+f;
    f = diff(a21,diff(a21,f))/12+diff(a21,f)/2+f;
    f = diff(a31,diff(a31,f))/12+diff(a31,f)/2+f;
    f = diff(a32,diff(a32,f))/12+diff(a32,f)/2+f;
    print toString f
    '''.format(line)

    ehr = macaulay2.eval(code)
    print(ehr)