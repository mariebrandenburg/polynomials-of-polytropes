from sage.all import *

#file1 = open("polynomials/result_step2_1_9999.txt","r")
file2 = open("volume_polys_from_10000.txt","r")
file3 = open("output_vectors","w")

R = PolynomialRing(QQ,['a'+str(i)+str(j) for i in range(1,6) for j in range(1,6) if not i==j])
a12,a13, a14, a15, a21, a23, a24, a25, a31, a32, a34, a35, a41, a42, a43, a45, a51, a52, a53, a54 = R.gens()
reference_vector = [tuple(x) for x in WeightedIntegerVectors(4, [1]*20)]
vectors = []
count = 0

for line in file2.readlines():
    f = R(line)
    new_dict = {}
    for key, value in f.dict().items():
        new_dict[tuple(list(key))]=value
    v = [0]*len(reference_vector)
    for key in new_dict.keys():
        index = reference_vector.index(key)
        v[index] = new_dict.get(key)
    #vectors.append(v)
    file3.write(str(v)+"\n")
    count += 1
    if count % 100 == 0:
        print(count)
