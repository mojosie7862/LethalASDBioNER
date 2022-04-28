# ANLY 521 Final Project - Analysis of Embryonic Lethal ASD Biology via BioNER
by: Josephine Millard

## Instructions
####The first step was to extract the corpus of interest.

Embryonic lethal ASD geneset was curated from AutDB (https://gene.sfari.org/) and IMPC (https://www.mousephenotype.org/data/embryo) - **`network_timepoint_groups.csv`**
For this project the 58 embryonic lethal genes were used. 

Geneset was input to UniProt retrieve/IDmapping interface (https://www.uniprot.org/uploadlists/) to get all UniProt protein accessions for this gene set.
* **`uniprot-ids.txt`**

PMIDs corresponding to each uniprot identifier were requested from the UniProt XML entry
* **`python uniprotXMLrequest.py > lethal_pmids.txt`**

####Pubtator and ScispaCy models were used for BioNER

Pubtator model (repo: https://www.ncbi.nlm.nih.gov/research/pubtator/api.html)
* **`python ExampleCode.Python/SubmitPMIDList.py lethal_pmids.txt pubtator > lethal_pubtator_annotations.txt`**

Processing of Pubtator lethal literature entities:
* **`process_lethal_abstracts.py`**

ScispaCy model
* **`pip install en_core_sci_sm-0.5.0.tar.gz`** 
* **`python run_scispacy.py > results_en_core_sci_sm`**
* The script above runs the model on the target data but does not return entity type. The data used for results was actually generated using the online demo of this model which uses entity linking to UMLS concepts. (https://scispacy.apps.allenai.org/)
  * **`scispacy_UMLSlinkage.csv`**

Processing of ScispaCy lethal literature entities:
* **`process_scispacy_results.py`**

