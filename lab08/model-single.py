from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

template='2p31' 
chain='A'

tc=template+chain

class MyModel(automodel):
	def get_model_filename(self, sequence, id1, id2, file_ext):
		return sequence+'_'+`id2`+file_ext
	def special_restraints(self, aln): 
		rsr = self.restraints
a = MyModel(env, alnfile='target-'+tc+'.ali',
 	knowns=tc,
 	sequence='target',
 	assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 5 
a.make()