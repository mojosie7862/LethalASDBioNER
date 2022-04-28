import scispacy
import spacy
from spacy import displacy
from scispacy.linking import EntityLinker

nlp = spacy.load("en_core_sci_sm", )
text = open('abstracts.txt').read().strip()
doc = nlp(text)
nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})

print(doc.ents)
