from pgmpy.inference import VariableElimination, ApproxInference
from pgmpy.sampling import BayesianModelSampling
from pgmpy.factors.discrete import State

from network import bayes_network


if __name__ == "__main__":
	solver = VariableElimination(bayes_network)
	print(
		solver.query(
			variables=['income'], 
			evidence={'parents': 0, 'age': 2, 'smoking_period': 0, 'sport': 0, 'credit_worthiness': 0},
		)
	)

	inference = BayesianModelSampling(bayes_network)
	samples = inference.rejection_sample( # rejection_sample
		evidence=[State('parents', 0), State('age', 2), State('smoking_period', 0), State('sport', 0), State('credit_worthiness', 0)],
		size=1000000, 
		show_progress=False,
	)
	
	solver = ApproxInference(bayes_network)
	print(
		solver.query(
			variables=['income'], 
			evidence={'parents': 0, 'age': 2, 'smoking_period': 0, 'sport': 0, 'credit_worthiness': 0},
			samples=samples, 
			show_progress=False,
		)
	)
