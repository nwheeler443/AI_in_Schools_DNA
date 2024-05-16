#! /usr/bin/env python3

# generate a random DNA sequence of a given length
import random
import pandas as pd

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

def show_table(df):
    return df.apply(pd.to_numeric).style.format('{0:,.1f}').background_gradient(cmap ='RdBu', vmin=-5, vmax=5).set_properties(**{'font-size': '8px'}).set_table_styles([
                            {"selector":"thead", "props": [("font-size", "4px")]}, {"selector":"th.row_heading", "props": [("font-size", "10px")]},])

def show_frequency_table(df):
    return df.style.background_gradient(cmap ='Blues').set_properties(**{'font-size': '10px'})

def show_scores(df):
    return df.apply(pd.to_numeric).style.format('{0:,.1f}').background_gradient(cmap ='RdBu_r', vmin=-5, vmax=5).set_properties(**{'font-size': '8px'}).set_table_styles([
                            {"selector":"thead", "props": [("font-size", "8px")]}, {"selector":"th.row_heading", "props": [("font-size", "10px"), ("width", "100")]},])
