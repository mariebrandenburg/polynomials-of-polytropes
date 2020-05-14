from sage.all import *

file1 = open("polynomials/output_vectors_1_9999","r")
file2 = open("polynomials/output_vectors_10000","r")

m = matrix(ZZ,[[1]+eval(line) for line in file1.readlines()]+[[1]+eval(line) for line in file2.readlines()])
print("number of rows: "+str(m.nrows()))
n = m.transpose()
print("transpose done")
k = n.kernel()
d = k.dimension()
print("dimension of kernel: "+str(d))
aff = n.ncols()-k.dimension()-1
print("dimension of affine span: "+str(aff))