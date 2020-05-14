from sage.all import *
import numpy as np

def lattice_polytope(line):
    input_data = line.rstrip()
    input_data = input_data[1:len(input_data)-1].split('[')
    data_as_strings = []
    for vec in input_data:
        if len(vec):
            data_as_strings.append(vec[:vec.index(']')])

    #extract fractions and convert to lists representing rational numbers
    denominators = []
    data_rat = []
    for string in data_as_strings:
        string = string.split(',')
        numbers = []
        for number in string[1:]:
            if '/' in number:
                numerator = int(number[:number.index('/')].strip())
                denominator = int(number[number.index('/')+1:].strip())
                denominators.append(denominator)
                numbers.append([numerator,denominator])
            else:
                numbers.append([int(number)])
        data_rat.append(numbers)


    multiple = np.lcm.reduce(denominators)
    data_int = []

    #convert to integer matrix
    for vec in data_rat:
        vector_int = []
        for rat_number in vec:
            if len(rat_number)==1:
                vector_int.append(rat_number[0]*multiple)
            else:
                vector_int.append(int(rat_number[0]*multiple/rat_number[1]))
        data_int.append(vector_int)

    return Polyhedron(vertices = data_int)



input_file_multi  = open("vol_pols_3d","r")
input_file_kleene  = open("kleene_1_9999","r")
input_file_kleene_10000  = open("kleene_10000","r")
input_file_coords = open("data")
output_file_vols = open("output_comparison_vol", "w")


coords = input_file_coords.readlines()
multi_vol = input_file_multi_vol_1_9999.readlines()+input_file_multi_vol_10000.readlines()
weights = [line.split(';')[0] for line in input_file_kleene_1_9999.readlines()] + [line.split(';')[0] for line in input_file_kleene_10000.readlines()]

R = PolynomialRing(QQ, ','.join(['a'+str(i)+str(j) for i in range(1,6) for j in range(1,6) if not i==j]+['t']))


for index in range(len(multi_vol)):
    if index % 500 == 0:
        print(index)
    f = R(multi_vol[index])
    P = lattice_polytope(coords[index])
    Vol = 24 * P.affine_hull().volume()
    w = [int(x) for x in weights[index][1:-1].split(',')]+[1]
    output_file_vols.write(str(Vol==f(w))+'\n')
    

input_file_multi_vol_1_9999.close()
input_file_multi_vol_10000.close()
input_file_kleene_1_9999.close()
input_file_kleene_10000.close()
input_file_coords.close()
output_file_vols.close()
