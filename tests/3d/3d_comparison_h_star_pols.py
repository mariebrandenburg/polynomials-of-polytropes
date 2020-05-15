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

    if len(denominators):
        multiple = np.lcm.reduce(denominators)
    else:
        multiple = 1
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

    return Polyhedron(vertices = data_int, backend='normaliz')



with open("../../output/3d/3d_h_star_pols.txt","r") as input_file_multi:
    multi = input_file_multi.readlines()

with open("../../output/3d/3d_kleene_stars.txt","r") as input_file_kleene:
    weights = [line.split(';')[0] for line in input_file_kleene.readlines()]

with open("../../input/3d_data.txt","r") as input_file_coords:
    coords = input_file_coords.readlines()





R = PolynomialRing(QQ, ','.join(['a'+str(i)+str(j) for i in range(1,5) for j in range(1,5) if not i==j]+['t']))


for index in range(len(multi)):
    w = [int(x) for x in weights[index][1:-1].split(',')]
    f = R(multi[index])
    P = lattice_polytope(coords[index])
    g = P.ehrhart_series().numerator()
    if index == 0:
        mode = 'w'
    else:
        mode = "a"
    with open("3d_output_comparison_h_star.txt", mode) as output_file:
        output_file.write(str(R(g)==f(w+[R('t')]))+'\n')


