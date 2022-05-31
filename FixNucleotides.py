#Replace nucleotide y with N
import os, sys

os.chdir('C:/Users/julie/OneDrive/Skrivebord/Molekylær evolution/Exam/Dataset1')

infile = open('sequences1_headers.fasta', 'r')
outfile = open('dataset1.fasta', 'w')

all_count = 0
nv_count = 0
for line in infile:
    if not line.startswith('>'):
        for base in line:
            if base not in ['A', 'T', 'C','G', '\n']:
                outfile.write('N')
                nv_count += 1
            else:
                outfile.write(base)
    else:
        outfile.write(line)
        
    all_count += 1
        
print(str(nv_count) + ' non-valid bases found')
print(str(all_count) + ' bases found in total')
        
infile.close()
outfile.close()