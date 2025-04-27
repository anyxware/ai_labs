from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

bayes_network = BayesianNetwork()

bayes_network.add_node('income')
bayes_network.add_node('age')
bayes_network.add_node('future_income')
bayes_network.add_node('health')
bayes_network.add_node('smoking_period')
bayes_network.add_node('assets')
bayes_network.add_node('sport')
bayes_network.add_node('payment_history')
bayes_network.add_node('parents')
bayes_network.add_node('credit_worthiness')
bayes_network.add_node('reliability')
bayes_network.add_node('debt_to_income')

bayes_network.add_edge('assets', 'future_income')
bayes_network.add_edge('income', 'future_income')
bayes_network.add_edge('age', 'health')
bayes_network.add_edge('smoking_period', 'health')
bayes_network.add_edge('sport', 'health')
bayes_network.add_edge('income', 'assets')
bayes_network.add_edge('parents', 'assets')
bayes_network.add_edge('age', 'payment_history')
bayes_network.add_edge('debt_to_income', 'payment_history')
bayes_network.add_edge('reliability', 'credit_worthiness')
bayes_network.add_edge('future_income', 'credit_worthiness')
bayes_network.add_edge('debt_to_income', 'credit_worthiness')
bayes_network.add_edge('payment_history', 'reliability')
bayes_network.add_edge('age', 'reliability')
bayes_network.add_edge('health', 'reliability')

cpd_income = TabularCPD('income', 3,
	values=[
		[0.2], # high
		[0.5], # medium
		[0.3], # low
	],
)

cpd_age = TabularCPD('age', 3,
	values=[
		[0.2], # between_16_and_21
		[0.5], # between_22_and_64
		[0.3], # over_65
	],
)

cpd_future_income = TabularCPD('future_income', 2,
	values=[
		[0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1], # promising
		[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], # not_promising
	],
	evidence=['assets', 'income'],
	evidence_card=[3, 3],
)

cpd_health = TabularCPD('health', 3,
	values=[
		[0.6, 0.5, 0.5, 0.4, 0.4, 0.3, 0.5, 0.4, 0.4, 0.3, 0.3, 0.2, 0.4, 0.3, 0.3, 0.2, 0.2, 0.1], # good
		[0.35, 0.4, 0.4, 0.45, 0.45, 0.5, 0.4, 0.45, 0.45, 0.5, 0.5, 0.55, 0.45, 0.5, 0.5, 0.55, 0.55, 0.6], # normal
		[0.05, 0.1, 0.1, 0.15, 0.15, 0.2, 0.1, 0.15, 0.15, 0.2, 0.2, 0.25, 0.15, 0.2, 0.2, 0.25, 0.25, 0.3], # bad
	],
	evidence=['age', 'smoking_period', 'sport'],
	evidence_card=[3, 3, 2],
)

cpd_smoking_period = TabularCPD('smoking_period', 3,
	values=[
		[0.3], # never
		[0.35], # sometimes
		[0.35], # always
	],
)

cpd_assets = TabularCPD('assets', 3,
	values=[
		[0.8, 0.5, 0.4, 0.7, 0.4, 0.3, 0.6, 0.3, 0.1], # high
		[0.1, 0.3, 0.4, 0.15, 0.35, 0.4, 0.2, 0.3, 0.3], # medium
		[0.1, 0.2, 0.2, 0.15, 0.25, 0.3, 0.2, 0.4, 0.6], # low
	],
	evidence=['income', 'parents'],
	evidence_card=[3, 3],
)

cpd_sport = TabularCPD('sport', 2,
	values=[
		[0.5], # yes
		[0.5], # no
	],
)

cpd_payment_history = TabularCPD('payment_history', 3,
	values=[
		[0.15, 0.1, 0.3, 0.2, 0.4, 0.35], # excellent
		[0.25, 0.2, 0.4, 0.3, 0.5, 0.45], # acceptable
		[0.6, 0.7, 0.3, 0.5, 0.1, 0.2], # unacceptable
	],
	evidence=['age', 'debt_to_income'],
	evidence_card=[3, 2],
)

cpd_parents = TabularCPD('parents', 3,
	values=[
		[0.05], # rich
		[0.7], # normal
		[0.25], # poor
	],
)

cpd_credit_worthiness = TabularCPD('credit_worthiness', 2,
	values=[
		[0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2], # positive
		[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], # negative
	],
	evidence=['reliability', 'future_income', 'debt_to_income'],
	evidence_card=[2, 2, 2],
)

cpd_reliability = TabularCPD('reliability', 2,
	values=[
		[0.7, 0.6, 0.5, 0.8, 0.7, 0.6, 0.9, 0.8, 0.7, 0.4, 0.3, 0.2, 0.5, 0.4, 0.3, 0.6, 0.5, 0.4, 0.1, 0.1, 0.0, 0.2, 0.1, 0.0, 0.3, 0.2, 0.1], # reliable
		[0.3, 0.4, 0.5, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3, 0.6, 0.7, 0.8, 0.5, 0.6, 0.7, 0.4, 0.5, 0.6, 0.9, 0.9, 1.0, 0.8, 0.9, 1.0, 0.7, 0.8, 0.9], # unreliable
	],
	evidence=['payment_history', 'age', 'health'],
	evidence_card=[3, 3, 3],
)

cpd_debt_to_income = TabularCPD('debt_to_income', 2,
	values=[
		[0.4], # low
		[0.6], # high
	],
)

bayes_network.add_cpds(
	cpd_income,
	cpd_age,
	cpd_future_income,
	cpd_health,
	cpd_smoking_period,
	cpd_assets,
	cpd_sport,
	cpd_payment_history,
	cpd_parents,
	cpd_credit_worthiness,
	cpd_reliability,
	cpd_debt_to_income,
)
