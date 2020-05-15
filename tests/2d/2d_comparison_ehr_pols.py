from sage.all import *



with open("../../output/2d/2d_ehr_pols.txt","r") as input_file_multi_ehr:
    multi_ehr = input_file_multi_ehr.readlines()

with open("../../output/2d/2d_kleene_stars.txt","r") as input_file_kleene:
    weights = [line.split(';')[0] for line in input_file_kleene.readlines()]

with open("2d_erhart_test_data","r") as input_file_ehrhart_test:
    ehr_test = input_file_ehrhart_test.readlines()


R = PolynomialRing(QQ, ','.join(['a'+str(i)+str(j) for i in range(1,4) for j in range(1,4) if not i==j]+['t']))


for index in range(len(multi_ehr)):
    f = R(multi_ehr[index])
    g = R(ehr_test[index])
    w = [int(x) for x in weights[index][1:-1].split(',')]+[1]
    if index == 0:
        mode = 'w'
    else:
        mode = "a"
    with open("2d_output_comparison_ehr.txt", mode) as output_file:
        output_file.write(str(g==f([x*R('t') for x in w]))+'\n')
    