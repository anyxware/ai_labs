class Node:
	def __init__(self):
		self.parents = set()
		self.childs = set()

	def add_parent(self, parent_node_name):
		self.parents.add(parent_node_name)

	def add_child(self, child_node_name):
		self.childs.add(child_node_name)

	def add_cpd(self, cpd):
		self.cpd = cpd


class TabularCPD:
	def __init__(self, name, states, values, evidence, evidence_card):
		self.name = name
		self.states = states
		self.values = values
		self.evidence = evidence
		self.evidence_card = evidence_card


class BayesianNetwork:
	def __init__(self):
		self.nodes = {}

	def add_node(self, node_name):
		if node_name in self.nodes:
			return

		self.nodes[node_name] = Node()

	def add_edge(self, src_node_name, dst_node_name):
		if not src_node_name in self.nodes:
			raise Exception(f"invalid node name: {src_node_name}")

		if not dst_node_name in self.nodes:
			raise Exception(f"invalid node name: {dst_node_name}")

		self.nodes[src_node_name].add_child(dst_node_name)
		self.nodes[dst_node_name].add_parent(src_node_name)

	def add_cpds(self, *cpds):
		for cpd in cpds:
			self.nodes[cpd.name].add_cpd(cpd)
