from modeller import *
from modeller.automodel import *

env = environ()
aln = alignment(env)

template='2p31'
chain='A'

tc=template+chain

mdl = model(env, file=template, 
model_segment=('FIRST:'+chain,'LAST:'+chain)) 
aln.append_model(mdl, align_codes=tc, atom_files=template+'.pdb') 
aln.append(file='target.ali', align_codes='target') 
aln.align2d()
aln.write(file='target-'+tc+'.ali', alignment_format='PIR') 
aln.write(file='target-'+tc+'.pap', alignment_format='PAP')
