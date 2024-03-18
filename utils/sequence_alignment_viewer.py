#! /usr/bin/env python3
# adapted from https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner

import numpy as np

import panel as pn
import panel.widgets as pnw
pn.extension()

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Plot, Grid, Range1d
from bokeh.models.glyphs import Text, Rect
from bokeh.layouts import gridplot

def view_alignment(sequences, language='DNA', fontsize="9pt", plot_width=800):
    """Bokeh sequence alignment view"""
    # sort sequences dictionary by key
    seqs = list(sequences.values())
    seqs.reverse()
    ids = list(sequences.keys())
    ids.reverse()

    #make sequence and id lists from the aln alignment
    text = [i for s in seqs for i in s]
    colors = get_colors(seqs, language=language)    
    N = len(seqs[0])
    S = len(seqs)    
    width = .4

    x = np.arange(0.5,N+0.5)
    y = np.arange(0,S,1)
    #creates a 2D grid of coords from the 1D arrays
    xx, yy = np.meshgrid(x, y)
    #flattens the arrays
    gx = xx.ravel()
    gy = yy.flatten()
    #use recty for rect coords with an offset
    recty = gy+.5
    h= 1/S
    #now we can create the ColumnDataSource with all the arrays
    source = ColumnDataSource(dict(x=gx, y=gy, recty=recty, text=text, colors=colors))
    plot_height = len(seqs)*15+50
    x_range = Range1d(0,N+1, bounds='auto')
    if N>100:
        viewlen=100
    else:
        viewlen=N
    #view_range is for the close up view
    view_range = (0,viewlen)
    tools="xpan, xwheel_zoom, reset, save" 

    #sequence text view with ability to scroll along x axis
    p = figure(title=None, width=plot_width, height=plot_height,
                x_range=view_range, y_range=ids, tools="xpan,reset",
                min_border=0, toolbar_location='below')#, lod_factor=1)          
    glyph = Text(x="x", y="y", text="text", text_align='center',text_color="black",
                text_font="monospace",text_font_size=fontsize)
    rects = Rect(x="x", y="recty",  width=1, height=1, fill_color="colors",
                line_color=None, fill_alpha=0.4)
    p.add_glyph(source, glyph)
    p.add_glyph(source, rects)

    p.grid.visible = False
    p.xaxis.major_label_text_font_style = "bold"
    p.yaxis.minor_tick_line_width = 0
    p.yaxis.major_tick_line_width = 0

    p = gridplot([[p]], toolbar_location='below')
    return p

def get_colors(seqs, language):
    """make colors for bases in sequence"""
    text = [i for s in list(seqs) for i in s]
    if language == 'DNA':
        clrs =  {'A':'red','T':'green','G':'orange','C':'blue','-':'white'}
    if language == 'protein':
        clrs =  {'A':'red','L':'red','I':'red','V':'red','M':'red','F':'red','Y':'red','W':'red', # hydrophobic
                 'H':'blue','K':'blue','R':'blue', # basic
                 'D':'green','E':'green', # acidic
                 'S':'orange','T':'orange','N':'orange','Q':'orange', # polar
                 'C':'pink','U':'pink','G':'pink','P':'pink', # special cases
                 '-':'white', '*':'black'}
    colors = [clrs[i] for i in text]
    return colors