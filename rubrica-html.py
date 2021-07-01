#!/usr/bin/python
# Author: Alfredo Sánchez Alberca (asalber@ceu.es)

import pandas as pd 
rubrics = {'Estadística y Probabilidad':'rubrica-estadistica'}

def get_chapters(file_name):
  df = pd.read_csv(file_name)
  return pd.unique(df.Tema)

def summary(file_name):
  df = pd.read_csv(file_name)
  chapters = pd.unique(df.Tema)
  return df.Tema.value_counts().reindex(chapters).rename('Num Items').to_markdown()

def items_table(file_name, chapter):
  df = pd.read_csv(file_name)
  return df[df.Tema == chapter].iloc[:,1:].to_markdown()

md = ''
for k, v in rubrics.items():
  md += '- [' + k + '](' + v + '.html)\n' 
f = open('docs/index.md', 'w')
f.write(md)
f.close()

for k, v in rubrics.items():
  md = '# Rúbrica de ' + k + '\n\n'
  md += summary(v + '.csv')
  for i in get_chapters(v + '.csv'):
    md += '\n\n# ' + i + '\n\n'
    md += items_table(v + '.csv', i)

  f = open('docs/' + v + '.md', 'w')
  f.write(md)
  f.close()
