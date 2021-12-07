
import ruamel.yaml
yaml = ruamel.yaml.YAML()
import json

def example_to_nluyml(infile,outfile):
	if infile.endswith('.yml'):
		try:
			with open(infile) as fp:
				data1 = yaml.load(fp)
				print(data1['intent'],"intent given")
		except YAMLError as exc:
			print(exc)
	elif infile.endswith('.json') or infile.endswith('.txt'):
		try:
			with open(infile) as fp:
				data1 = json.load(fp)
				print(data1['intent'],"intent given")
		except Exception as e:
			print(e)
	
	yaml.default_flow_style=None
	
	try:
		with open(outfile) as fp:
			data = yaml.load(fp)
			for entry in data['nlu']:
				if entry['intent'] == data1['intent']:
					print(entry['examples'],"existing examples")
					entry['examples'] += data1['examples']
					print(entry,"new updated examples")
			yaml.dump(data,open(outfile, 'w'))
	except Exception as e:
		print(e)

'''
	out1 is called for yml to yml file
'''
out1 = example_to_nluyml("example.yml","nlu.yml")

'''
	out2 is called for json to yml file
'''		
# out2 = example_to_nluyml('example_json.json','nlunew.yml')

'''
	out 3 is called for txt file to yml file
'''
# out3 = example_to_nluyml('examples.txt','nlunew.yml')