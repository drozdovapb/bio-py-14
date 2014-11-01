fastafile = input()

with open(fastafile, 'r') as ffh:
    fastaseq = list(); names = list()
    i = -1
    for line in ffh:
        if line[0] == '>':
            print(line)
            names.append('')
            fastaseq.append('')
            i += 1
        else:
            fastaseq[i] += line.replace('\n', '')

sumseqlengths = 0
for seq in fastaseq:
    sumseqlengths = len(seq)
meanseqlengths = sumseqlengths / len(fastaseq)

print(len(fastaseq), 'sequences in the input file')
print('mean sequence length is', meanseqlengths)

def check_N(seq):
    seqflag = 0
    for symbol in seq:
        if symbol == 'N' or symbol == 'n':
            return False
    return True

Ns = 0
for seq in fastaseq:
    Ns += check_N(seq)

print(Ns, 'sequences without Ns')

print('The beginnings and endings of the three longest sequences are below')

longestseq = max(fastaseq)
print(longestseq[0:19], '...', longestseq[-20:-1])

fastaseq2 = fastaseq[:]
fastaseq2.remove(longestseq)
secondlongest = max(fastaseq2)
print(secondlongest[0:19], '...', secondlongest[-20:-1])

fastaseq3 = fastaseq2[:]
fastaseq3.remove(secondlongest)
thirdlongest = max(fastaseq3)
print(thirdlongest[0:19], '...', thirdlongest[-20:-1])

#print("that's it")
