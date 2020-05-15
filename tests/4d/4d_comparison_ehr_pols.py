from sage.all import *


def get_input(line_number):
    ## manage the jungle of input files

    line_number_multi = line_number
    if index < 9999:
        fname_multi = '../../output/4d/4d_ehr_pols_1_9999.txt'
    else:
        fname_multi = '../../output/4d/4d_ehr_pols_10000.txt'
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

    line_number_univ = line_number
    if index < 9999:
        fname_weight = '4d_ehrhart_test_data_1_9999.txt'
    else:
        fname_weight = '4d_ehrhart_test_data_10000.txt'
        line_number_univ  -= 9999
    with open(fname_weight) as fp:
        for i, line in enumerate(fp):
            if i == line_number_univ:
                univ = line
                break       

    return univ, multi, weight


R = PolynomialRing(QQ, ','.join(['a'+str(i)+str(j) for i in range(1,6) for j in range(1,6) if not i==j]+['t']))


for index in range(27247):
#for index in range(9997,10003):
#for index in range(5):
    univ, multi, weight = get_input(index)
    f = R(multi)
    g = R(univ)
    w = [int(x) for x in weight[1:-1].split(',')]+[1]
    if index == 0:
        mode = 'w'
    else:
        mode = "a"
    with open("4d_output_comparison_ehr.txt", mode) as output_file:
    	output_file.write(str(g==f([x*R('t') for x in w]))+'\n')
    
