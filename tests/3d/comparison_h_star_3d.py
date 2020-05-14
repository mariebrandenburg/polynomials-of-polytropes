# Python program killing 
# a thread using multiprocessing 
# module 
  
import multiprocessing 
from sage.all import *
import numpy as np

def lattice_polytope(line):
    ## take coordinates of a rational polytope as input
    ## dilate the coordinates to make them integer
    ## return the smallest integer lattice polytope that is a dilation of the input

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

    return Polyhedron(vertices = data_int, backend='normaliz')


def get_input(line_number):
    ## manage the jungle of input files

    with open('data') as fp:
        for i, line in enumerate(fp):
            if i == line_number:
                coord = line
                break

    line_number_multi = line_number
    if index < 9999:
        fname_multi = 'h_star_1_9999'
    elif index < 20000:
        fname_multi = 'h_star_10000_19999'
        line_number_multi -= 9999
    else:
        fname_multi = 'h_star_20000'
        line_number_multi -= 20000
    with open(fname_multi) as fp:
        for i, line in enumerate(fp):
            if i == line_number_multi:
                multi = line
                break
    
    line_number_kleene = line_number
    if index < 9999:
        fname_weight = 'kleene_1_9999'
    else:
        fname_weight = 'kleene_10000'
        line_number_kleene  -= 9999
    with open(fname_weight) as fp:
        for i, line in enumerate(fp):
            if i == line_number_kleene:
                weight = line.split(';')[0]
                break

    return coord, multi, weight



def comparison(coord, weight, multi, pipe):
    ## compute the univariate h*-polynomial of the lattice polytope P
    ## evaluate the multivariate h*-polynoial at the weight vector weight*t
    ## compare the evaluated multivariate with the univariate h*-polynomial
    GENS_STR = ['a'+str(i)+str(j) for i in range(1,6) for j in range(1,6) if not i==j]
    R = PolynomialRing(QQ, 't')
    P = lattice_polytope(coord)
    univ = P.ehrhart_series().numerator()

    w = [int(x) for x in weight[1:-1].split(',')]
    for index2 in range(len(w)):
        multi = multi.replace(GENS_STR[index2], "("+str(w[index2])+")")

    f = R(multi)
    g = R(univ)
    pipe.send(g==f)




MAX_WAITING_TIME = 7 * 60
CHECK_INTERVAL = 10
## start computing the comparison for each line
## check every CHECK_INTERVAL seconds for a result
## kill the process after MAX_WAITING_TIME seconds otherwise
for index in range(27247):
    if not index % 1000:
        print('index',index)

    recv_end, send_end = multiprocessing.Pipe(False)
    coord, multi, weight = get_input(index)
    p = multiprocessing.Process(
        target=comparison, 
        args=(coord, weight, multi, send_end)
    )
    p.start()

    waiting_time = 0
    result = '?'
    while(waiting_time < MAX_WAITING_TIME):
        if recv_end.poll(CHECK_INTERVAL):
            result = str(recv_end.recv())
            p.join()
            break
        waiting_time += CHECK_INTERVAL

    if p.is_alive():
        p.terminate()
    
    write_mode = 'w' if index == 0 else 'a'
    with open("output_comparison_h_star", write_mode) as fp:
        fp.write(result+'\n')