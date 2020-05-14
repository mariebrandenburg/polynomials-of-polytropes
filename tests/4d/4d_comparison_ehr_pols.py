from sage.all import *

input_file_1  = open("output","r")
input_file_2  = open("result_step1","r")
input_file_3 = open("erhart_tests","r")
output_file = open("output_comparison", "w")

multi_ehr = input_file_1.readlines()
weights = [line.split(';')[0] for line in input_file_2.readlines()]
ehr_test = input_file_3.readlines()

R = PolynomialRing(QQ, ','.join(['a'+str(i)+str(j) for i in range(1,6) for j in range(1,6) if not i==j]+['t']))


for index in range(len(multi_ehr)):
    f = R(multi_ehr[index])
    g = R(ehr_test[index])
    w = [int(x) for x in weights[index][1:-1].split(',')]+[1]
    output_file.write(str(g==f([x*R('t') for x in w]))+'+\n')
    
input_file_1.close()
input_file_2.close()
input_file_3.close()
output_file.close()