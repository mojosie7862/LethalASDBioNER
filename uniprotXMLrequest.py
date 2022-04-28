import xml.etree.ElementTree as ET
import pandas as pd
import urllib.request


lethal_sets_df = pd.read_csv('uniprot-ids.txt', delimiter='\t')
lethal_set = list(lethal_sets_df['Entry'].dropna())
ns = '{http://uniprot.org/uniprot}'
pmids = {}
for acc in lethal_set:
    thefile = urllib.request.urlopen('http://www.uniprot.org/uniprot/'+acc+'.xml')
    tree_document = ET.parse(thefile)
    root = tree_document.getroot()
    ent_ele = root.find(ns + 'entry')
    refs = []
    for ele in ent_ele.findall(ns + 'reference'):
        cit_ele = ele.find(ns + 'citation')
        for ref in cit_ele.findall(ns + 'dbReference'):
            if ref.attrib['type'] == 'PubMed':
                refs.append(ref.attrib['id'])
    pmids[acc] = refs

flat_pmids = [item for sublist in pmids.values() for item in sublist]

for i in flat_pmids:
    print(i)



