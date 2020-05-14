import sys
from sage.interfaces.macaulay2 import Macaulay2

macaulay2 = Macaulay2()

for line in sys.stdin:
    line = line.rstrip()
    code = '''
    S = QQ[a12,a13,a14,a15,a21,a23,a24,a25,a31,a32,a34,a35,a41,a42,a43,a45,a51,a52,a53,a54];
    vol = {};
    f = vol/24;
    f = diff(a12, diff(a12, diff(a12, diff(a12,f))))/(24*(-30)) + diff(a12, diff(a12, f))/12 + diff(a12, f)/2 + f;
    f = diff(a13, diff(a13, diff(a13, diff(a13,f))))/(24*(-30)) + diff(a13, diff(a13, f))/12 + diff(a13, f)/2 + f;
    f = diff(a14, diff(a14, diff(a14, diff(a14,f))))/(24*(-30)) + diff(a14, diff(a14, f))/12 + diff(a14, f)/2 + f;
    f = diff(a15, diff(a15, diff(a15, diff(a15,f))))/(24*(-30)) + diff(a15, diff(a15, f))/12 + diff(a15, f)/2 + f;
    f = diff(a21, diff(a21, diff(a21, diff(a21,f))))/(24*(-30)) + diff(a21, diff(a21, f))/12 + diff(a21, f)/2 + f;
    f = diff(a23, diff(a23, diff(a23, diff(a23,f))))/(24*(-30)) + diff(a23, diff(a23, f))/12 + diff(a23, f)/2 + f;
    f = diff(a24, diff(a24, diff(a24, diff(a24,f))))/(24*(-30)) + diff(a24, diff(a24, f))/12 + diff(a24, f)/2 + f;
    f = diff(a25, diff(a25, diff(a25, diff(a25,f))))/(24*(-30)) + diff(a25, diff(a25, f))/12 + diff(a25, f)/2 + f;
    f = diff(a31, diff(a31, diff(a31, diff(a31,f))))/(24*(-30)) + diff(a31, diff(a31, f))/12 + diff(a31, f)/2 + f;
    f = diff(a32, diff(a32, diff(a32, diff(a32,f))))/(24*(-30)) + diff(a32, diff(a32, f))/12 + diff(a32, f)/2 + f;
    f = diff(a34, diff(a34, diff(a34, diff(a34,f))))/(24*(-30)) + diff(a34, diff(a34, f))/12 + diff(a34, f)/2 + f;
    f = diff(a35, diff(a35, diff(a35, diff(a35,f))))/(24*(-30)) + diff(a35, diff(a35, f))/12 + diff(a35, f)/2 + f;
    f = diff(a41, diff(a41, diff(a41, diff(a41,f))))/(24*(-30)) + diff(a41, diff(a41, f))/12 + diff(a41, f)/2 + f;
    f = diff(a42, diff(a42, diff(a42, diff(a42,f))))/(24*(-30)) + diff(a42, diff(a42, f))/12 + diff(a42, f)/2 + f;
    f = diff(a43, diff(a43, diff(a43, diff(a43,f))))/(24*(-30)) + diff(a43, diff(a43, f))/12 + diff(a43, f)/2 + f;
    f = diff(a45, diff(a45, diff(a45, diff(a45,f))))/(24*(-30)) + diff(a45, diff(a45, f))/12 + diff(a45, f)/2 + f;
    f = diff(a51, diff(a51, diff(a51, diff(a51,f))))/(24*(-30)) + diff(a51, diff(a51, f))/12 + diff(a51, f)/2 + f;
    f = diff(a52, diff(a52, diff(a52, diff(a52,f))))/(24*(-30)) + diff(a52, diff(a52, f))/12 + diff(a52, f)/2 + f;
    f = diff(a53, diff(a53, diff(a53, diff(a53,f))))/(24*(-30)) + diff(a53, diff(a53, f))/12 + diff(a53, f)/2 + f;
    f = diff(a54, diff(a54, diff(a54, diff(a54,f))))/(24*(-30)) + diff(a54, diff(a54, f))/12 + diff(a54, f)/2 + f;
    print toString f
    '''.format(line)

    ehr = macaulay2.eval(code)
    print ehr



