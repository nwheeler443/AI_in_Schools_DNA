#! /usr/bin/env python3

# generate a random DNA sequence of a given length
import random

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

