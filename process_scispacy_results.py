import pandas as pd

results_df = pd.read_csv('scispacy_UMLSlinkage.csv')

entities = list(results_df['Canonical Name'])
terms = list(results_df['text'])

just_ent_counts = {}
for e in entities:
    if e not in just_ent_counts.keys():
        just_ent_counts[e] = 1
    else:
        just_ent_counts[e] += 1

scispacy_results_1 = []
for en, coun in just_ent_counts.items():
    row = [en, coun]
    scispacy_results_1.append(row)

scispacy_result_df2 = pd.DataFrame(scispacy_results_1)
scispacy_result_df2.to_csv('scispacy_results_df2.csv')

count_dict = {}
for e,t in zip(entities, terms):
    if e not in count_dict.keys():
        count_dict[e] = {}
    if t not in count_dict[e]:
        count_dict[e][t] = 1
    else:
        count_dict[e][t] += 1
make_cnt_df = []
for x,y in count_dict.items():
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

scispacy_results = []
for group in make_cnt_df:
    typ = group[0]
    for term, count in zip(group[1], group[2]):
        row = [typ, term, count]
        scispacy_results.append(row)

scispacy_result_df = pd.DataFrame(scispacy_results)
scispacy_result_df.to_csv('scispacy_results_df.csv')

