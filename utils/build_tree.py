#! /usr/bin/env python3
# build a phylogenetic tree from a list of sequences

from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import re
from Bio import Phylo
from io import StringIO
import matplotlib.pyplot as plt
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


def build_tree(sequences, method='upgma'):
    # convert dictionary of aligned sequence strings to a list of SeqRecord objects
    sequence_list = [SeqRecord(Seq(seq), id=name) for name, seq in sequences.items()]
    # create a MultipleSeqAlignment object from the list of SeqRecord objects
    alignment = MultipleSeqAlignment(sequence_list)
    
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    
    constructor = DistanceTreeConstructor()
    if method == 'upgma':
        tree = constructor.upgma(dm)
    if method == 'nj':
        tree = constructor.nj(dm)
    
    tree.root_with_outgroup('Ancestor')
    tree.ladderize() # place longer branches on the bottom
    edit_tree = re.sub('Inner\\d+', '', tree.format('newick')) # remove the inner node labels
    handle = StringIO(edit_tree)
    tree = Phylo.read(handle, 'newick')
    fig = plt.figure(figsize=(10, 10), dpi=100)
    axes = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=axes)
    
    return alignment
