import sys
sys.path.append("..")

from pcs import PCS
from chain import Chain

tool = PCS()
output_file = "closed_chain_analysis_500_7_17_4.csv"
data = open("output/" + output_file, "w")
data.write("pcs;prime forme;closed p;closable p;average size\n")
attempts = 500
link_min = 7
link_max = 17
degrading = 4

print("Let's check how easy is to obtain a closed chain for all prime forms.", end="\n")
print("I am configured with the following parameters:", end="\n")
print("attempts: " + str(attempts), end="\n")
print("minimum links: " + str(link_min), end="\n")
print("maximum links: " + str(link_max), end="\n")
print("accepted degrading: " + str(degrading), end="\n\n")

def prime_form_to_string(prime_form):
	s = ""
	for n in prime_form:
		s += str(n)
		s += " "
	return s[:len(s)-1]

def write_data_line(the_set, prime_form_string, interval_vector, closed_probability, closable_probability, average_size):
	line = the_set + ";"
	line += prime_form_string + ";"
	line += interval_vector +";"
	line += str(closed_probability) + ";"
	line += str(closable_probability) + ";"
	line += str(average_size) + "\n"
	data.write(line)

def new_chain_set(the_set, prime_form_string, interval_vector):
	ch = Chain(tool, prime_form_string, link_min, link_max, degrading)
	closed_chains = 0
	closable_chains = 0
	chains_size = 0
	for i in range(attempts):
		if ch.is_closed:
			closed_chains += 1
		if ch.is_closable:
			closable_chains += 1
		chains_size += ch.sequence_size
		ch.run()
	write_data_line(the_set, prime_form_string, interval_vector, closed_chains/attempts, closable_chains/attempts, chains_size/attempts)


def chains_loop(cardinality, prime_forms):
	for i in range(len(prime_forms)):
		print("working on set " + str(cardinality) + "." + str(i+1), end="       \r")
		prime_form_string = prime_form_to_string(prime_forms[i])
		interval_vector = tool.vector_to_string(tool.interval_vector(prime_forms[i]))
		the_set = str(cardinality) + "." + str(i+1)
		new_chain_set(the_set, prime_form_string, interval_vector)

chains_loop(4, tool.prime_forms[3])
chains_loop(5, tool.prime_forms[4])
chains_loop(6, tool.prime_forms[5])
chains_loop(7, tool.prime_forms[6])
chains_loop(8, tool.prime_forms[7])
chains_loop(9, tool.prime_forms[8])

data.close()
print("I save the results at data/" + output_file, end="\n")