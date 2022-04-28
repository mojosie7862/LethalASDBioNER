def find_2nd(string, substring):
   return string.find(substring, string.find(substring) + 1)

# organize output of pubtator request
data = open('lethal_pubtator_annotations.txt').read()
data = data.replace(r'\n', '\n').replace(r'\t', '\t').split('\n') #replace escape sequences with string literals

#clean up request output
data[0] = data[0][2:]
data = data[:-2]

#make corpus of abstracts to run on scispacy
#make dictionary of named entities from pubtator model

entries = []
entry = []
for i in data:
    if len(i) != 0:
        i = i.split('\t')
        entry.append(i)
    else:
        entries.append(entry)
        entry = []

abstracts = []
NE_pubtator_dict = {'PMIDs': []}

for i, x in enumerate(entries):
    for idx,j in enumerate(x):
        if idx == 0:
            p1 = j[0].find('|')
            pmid = j[0][:p1]
            if pmid not in NE_pubtator_dict['PMIDs']:
                NE_pubtator_dict['PMIDs'].append(pmid)
        if idx == 1:
            p2 = find_2nd(j[0], '|')
            abs = j[0][p2+1:]
            abstracts.append(abs)
        if idx > 1:
            term = j[3]
            entity = j[4]
            ent_id = j[5] #not planning to use this but it's here if useful later
            if entity not in NE_pubtator_dict.keys():
                NE_pubtator_dict[entity] = []
            NE_pubtator_dict[entity].append(term)

abstracts = ''.join(abstracts)

#for printing to abstracts.txt
#print(abstracts)

print(NE_pubtator_dict.keys())

