#Change headers of fasta file
import sys, os

#Set working directory
os.chdir('C:/Users/julie/OneDrive/Skrivebord/Molekylær evolution/Exam/Dataset1')


#Read fasta and meta data files
fastaFile = open('sequences1.fasta', 'r')
metaFile = open('sequences1.csv', 'r')

#Open outfile
augmentedFastaFile = open('sequences1_headers.fasta', 'w')

#Save metadata in a dict
metaData = dict()
for line in metaFile:
    splitLine = line.split(',')
    accession = splitLine[0]
  
    #Remember how many columns there are supposed to be
    if accession == 'Accession':
        length = len(splitLine)
 
    
    #Read non-header lines
    else:
        #Error check
        if len(splitLine) != length:
            print('ERROR: Too many or too few columns for '+ accession)
            sys.exit(1)
        if accession in metaData:
            print('ERROR: Duplicate accession number: ' + accession)
            sys.exit(1)
            
        
        #Location
        if splitLine[4] == 'Democratic Republic of the Congo':
            location = 'DRC'
        elif splitLine[4].startswith('USA'):
            location = 'USA'
        elif splitLine[4].startswith('Nigeria'):
            location = 'Nigeria'
        elif splitLine[4].startswith('Cote'):
            location = 'Cote-dIvoire'
        else:
            location = '-'.join(splitLine[4].split(' '))
        
            
        #Collection date
        collDate = splitLine[-1][0:-1]
        if len(collDate.split('-')) == 2:
            collDate = collDate + '-15'
    
        #Add to dict    
        metaData[accession] = [collDate, location]
        
        
metaFile.close()


#Change headers in fasta file
for line in fastaFile:
    if line.startswith('>'):
        accession = line.split(' ')[0][1:-2]
        
        if accession in metaData:
            collDate = metaData[accession][0]
            location = metaData[accession][1]
            augmentedFastaFile.write('>' + accession + '_' + collDate + '_' + location + '\n')
        else:
            print('ERROR: Accession ' + accession + ' not found in meta data')
            sys.exit(1)
            
    else:
        augmentedFastaFile.write(line)

augmentedFastaFile.close()
