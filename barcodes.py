#!/usr/bin/env python3

import csv
import sys
from subprocess import call
from collections import OrderedDict

def multipleReplace(text, wordDict):
	for key in wordDict:
		text = text.replace(key, wordDict[key])
	return text

def buildPage(labelstex, pageNum):
	pagetex = pagetemplate.replace('<labels>', labelstex)
	tmpfilename = 'tmp' + "%08d" % pageNum
	tmptexfile = open(tmpfilename + '.tex', 'w')
	tmptexfile.write(pagetex)
	tmptexfile.close()
	call(['latex', tmpfilename + '.tex'])
	call(['dvips', tmpfilename + '.dvi'])
	call(['ps2pdf', tmpfilename + '.ps'])


latexspecialchars = OrderedDict(
	sorted({'\\':'\\textbackslash{}', #must come first
		'#':'\\#',
		'$':'\\$',
		'%':'\\%',
		'&':'\\&',
		'^':'\\textasciicircum{}',
		'_':'\\_',
		'{':'\\{',
		'}':'\\}',
		'~':'\\textasciitilde{}'}.items(),
		key = lambda t: int(t[0] != '\\')))

numlabels_x = 5
numlabels_y = 9
labels_per_page = numlabels_x * numlabels_y

# Load template for each label
labeltexfile = open('template_label.tex', 'r')
labeltemplate = labeltexfile.read()
labeltexfile.close()

# Load template for each page
pagetexfile = open('template_page.tex', 'r')
pagetemplate = pagetexfile.read()
pagetexfile.close()

# New page, empty contents
labelstex = ''

# Load data from CSV
with open(sys.argv[1], newline='', encoding='utf-8') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	i = 0
	for row in csvreader:
		item = {'<pos_x>'     : str(i % numlabels_x),
			'<pos_y>'     : str((i % labels_per_page) // numlabels_x),
			'<prod_ref>'  : multipleReplace(row[0], latexspecialchars),
			'<prod_name>' : multipleReplace(row[1].upper()[:35], latexspecialchars),
			'<cost>'      : '{:0.2f}'.format(float(row[2])).replace(',','tmp').replace('.',',').replace('tmp','.'),
			'<barcode>'   : row[3]}
		tmpstring = multipleReplace(labeltemplate, item)
		labelstex = labelstex + tmpstring
		i = i + 1
		if i % labels_per_page == 0:
			buildPage(labelstex, i / labels_per_page - 1)
			labelstex = ''

buildPage(labelstex, i / labels_per_page)
	
call('pdftk tmp*.pdf output labels.pdf', shell=True)
call('rm tmp*', shell=True)


	
