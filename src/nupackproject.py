from nupack import *
import random
import json

nbstrands = 1000
strandsize = 10
concentrations = [1e-5 for i in range(nbstrands)]

strands = []
sequences = []
for i in range(nbstrands):
    
    sequence = ''.join(random.choice("ACGT") for _ in range(strandsize))
    sequences.append(sequence)
    strand = Strand(sequence, name=sequence)
    strands.append(strand)
    
strandsdict = dict(zip(strands, concentrations)) 

t1 = Tube(strands=strandsdict, name='t1')
tube_results = tube_analysis(tubes=[t1], model=Model(material="dna"))

energypairs = []
for sequence in sequences:
    result = tube_results["("+sequence+")"]
    free_energy = result.free_energy
    pair = (sequence, free_energy)
    energypairs.append(pair)

print(energypairs)

with open('strandenergylist.json', 'w') as f:
    json.dump(energypairs, f)