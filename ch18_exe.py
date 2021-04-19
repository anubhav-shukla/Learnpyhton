# Anubhav salary is 1000000000000
#  Ashish salary is 10000

with open('n_sal.txt','r') as rf:
    with open('ns_print.txt','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')

            wf.write(f'{name}\'s salary is {salary}')

            #Hope now you understam=nd it.. 
