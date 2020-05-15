import sys
from sage.interfaces.macaulay2 import Macaulay2

macaulay2 = Macaulay2()

for line in sys.stdin:
    line = line.rstrip()
    code = '''
    S = QQ[a12,a13,a14,a21,a23,a24,a25,a31,a32,a34,a41,a42,a43];
    vol = {};
    f = vol/6;
    f = diff(a12, diff(a12, f))/12 + diff(a12, f)/2 + f;
    f = diff(a13, diff(a13, f))/12 + diff(a13, f)/2 + f;
    f = diff(a14, diff(a14, f))/12 + diff(a14, f)/2 + f;
    f = diff(a21, diff(a21, f))/12 + diff(a21, f)/2 + f;
    f = diff(a23, diff(a23, f))/12 + diff(a23, f)/2 + f;
    f = diff(a24, diff(a24, f))/12 + diff(a24, f)/2 + f;
    f = diff(a31, diff(a31, f))/12 + diff(a31, f)/2 + f;
    f = diff(a32, diff(a32, f))/12 + diff(a32, f)/2 + f;
    f = diff(a34, diff(a34, f))/12 + diff(a34, f)/2 + f;
    f = diff(a41, diff(a41, f))/12 + diff(a41, f)/2 + f;
    f = diff(a42, diff(a42, f))/12 + diff(a42, f)/2 + f;
    f = diff(a43, diff(a43, f))/12 + diff(a43, f)/2 + f;
    print toString f
    '''.format(line)

    ehr = macaulay2.eval(code)
    print(ehr)


