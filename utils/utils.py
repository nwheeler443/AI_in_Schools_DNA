#! /usr/bin/env python3

import random
import pandas as pd
import numpy as np

# generate a random DNA sequence of a given length
def random_DNA(length):
    DNA=""
    for count in range(length):
        DNA+=random.choice("CGTA")
    return DNA

# mutate a DNA sequence N times
def mutate_n(dna, N):
    dna = list(dna)
    for i in range(N):
        mutation_site = random.randint(0, len(dna) - 1)
        new_base = random.choice('ATCG')
        dna[mutation_site] = new_base
    return ''.join(dna)

def show_table(df,cols):
    return df.style.background_gradient(cmap ='RdBu', axis=None, gmap=cols, vmin=-5, vmax=5).set_tooltips(cols.round(1)).set_table_styles([{
     'selector': 'caption','props': 'font-size:1.25em;font-weight:bold'}], overwrite=False)

def show_frequency_table(df):
    return df.style.background_gradient(cmap ='Blues').set_properties(**{'font-size': '10px'}).set_table_styles([{
     'selector': 'caption',
     'props': 'font-size:1.25em;font-weight:bold'
 }], overwrite=False)

def show_scores(df):
    return df.apply(pd.to_numeric).style.format('{0:,.1f}').background_gradient(cmap ='RdBu_r', vmin=-5, vmax=5).set_properties(**{'font-size': '8px'}).set_table_styles([
                            {"selector":"thead", "props": [("font-size", "8px")]}, {"selector":"th.row_heading", "props": [("font-size", "10px"), ("width", "100")]},]).set_table_styles([{
     'selector': 'caption','props': 'font-size:1.25em;font-weight:bold'}], overwrite=False)


def calculate_match_score(sequence, amino_acid_frequencies):
    # create a list to store the match scores for each position in the sequence
    match_scores = []

    # for each position in the sequence
    for position in sequence.index:

        # find out the amino acid
        amino_acid = sequence[position]

        # get the frequencies of that amino acid in that position
        frequencies_pos = amino_acid_frequencies[str(position)][amino_acid]
        # get the frequencies of that amino acid across the whole protein
        frequencies_whole = amino_acid_frequencies['whole protein'][amino_acid]

        # calculate the odds ratio of the amino acid at that position in the sequence compared to the baseline
        # 1 - the frequency gives you the odds of not seeing a particular amino acid
        odds_ratio = (frequencies_pos / (1 - frequencies_pos)) / (frequencies_whole / (1 - frequencies_whole))

        import numpy as np # not recognising this for some reason
        # calculate the log of the score and add it to the list
        match_scores.append(np.log(odds_ratio))

    return match_scores

clrs =  {'A':'red','L':'#FA5F55','I':'#FA5F55','V':'#FA5F55','M':'#FA5F55','F':'#FA5F55','Y':'#FA5F55','W':'#FA5F55', # hydrophobic
                 'H':'#3395FF','K':'#3395FF','R':'#3395FF', # basic
                 'D':'#7DCEA0','E':'#7DCEA0', # acidic
                 'S':'#EB984E','T':'#EB984E','N':'#EB984E','Q':'#EB984E', # polar
                 'C':'#F5B7B1','U':'#F5B7B1','G':'#F5B7B1','P':'#F5B7B1', # special cases
                 '-':'white', '*':'black'}


def highlight_cells(x):
    return 'background-color: ' + x.map(clrs)

def view_alignment(df):
    return df.style.apply(highlight_cells)

