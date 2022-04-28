import pandas as pd

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
PMIDs = []
NE_pubtator_dict = {}

for i, x in enumerate(entries):
    for idx,j in enumerate(x):
        if idx == 0:
            p1 = j[0].find('|')
            pmid = j[0][:p1]
            if pmid not in PMIDs:
                PMIDs.append(pmid)
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
entity_counts = {}
for k,v in NE_pubtator_dict.items():
    if k not in entity_counts.keys():
        entity_counts[k] = {}
    for i in v:
        if i not in entity_counts[k]:
            entity_counts[k][i] = 1
        else:
            entity_counts[k][i] += 1
make_cnt_df = []
for x,y in entity_counts.items():
    df = []
    ent = []
    cnt = []
    df.append(x)
    for a,b in y.items():
        ent.append(a)
        cnt.append(b)
    df.append(ent)
    df.append(cnt)
    make_cnt_df.append(df)

pubtator_results = []
for group in make_cnt_df:
    typ = group[0]
    for term, count in zip(group[1], group[2]):
        row = [typ, term, count]
        pubtator_results.append(row)

pubtator_result_df = pd.DataFrame(pubtator_results)
pubtator_result_df.to_csv('pubtator_results_df.csv')
