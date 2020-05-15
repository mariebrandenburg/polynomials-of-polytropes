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

    if len(denominators)>0:
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

    return Polyhedron(vertices = data_int)



def get_input(line_number):
    ## manage the jungle of input files

    with open('../../input/4d_data.txt') as fp:
        for i, line in enumerate(fp):
            if i == line_number:
                coord = line
                break

    line_number_multi = line_number
    if index < 9999:
        fname_multi = '../../output/4d/4d_vol_pols_1_9999.txt'
    else:
        fname_multi = '../../output/4d/4d_vol_pols_10000.txt'
        line_number_multi -= 9999
    with open(fname_multi) as fp:
        for i, line in enumerate(fp):
            if i == line_number_multi:
                multi = line
                break
    
    line_number_kleene = line_number
    if index < 9999:
        fname_weight = '../../output/4d/4d_kleene_stars_1_9999.txt'
    else:
        fname_weight = '../../output/4d/4d_kleene_stars_10000.txt'
        line_number_kleene  -= 9999
    with open(fname_weight) as fp:
        for i, line in enumerate(fp):
            if i == line_number_kleene:
                weight = line.split(';')[0]
                break

    return coord, multi, weight



R = PolynomialRing(QQ, ','.join(['a'+str(i)+str(j) for i in range(1,6) for j in range(1,6) if not i==j]))


for index in range(27247):
#for index in range(9997,10003):
    if index % 500 == 0:
        print(index)
    coord, multi, weight = get_input(index)
    f = R(multi)
    P = lattice_polytope(coord)
    Vol = 24 * P.affine_hull().volume()
    w = [int(x) for x in weight[1:-1].split(',')]

    if index == 0:
        mode = 'w'
    else:
        mode = "a"
    with open("4d_output_comparison_vol_test.txt", mode) as output_file_vols:
        output_file_vols.write(str(Vol==f(w))+'\n')
    


