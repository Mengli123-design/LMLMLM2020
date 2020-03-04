#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--IDlist',help='input an seq ID list',required=True)
parser.add_argument('--ref',help='input a genome fa', required=True)
parser.add_argument('--out',help='output fasta',required=True)
args = parser.parse_args()

Reffa = args.ref
IDlist = args.IDlist
Outfile = args.out
Outfile = open(Outfile, 'w')
##############################
dict = {}
with open (Reffa, "r") as ref:
    for i in ref:
        line = i.strip().split(" ")[0]
        if line.startswith('>'):
            keys= line.replace(">","")
            dict[keys]=[]
        else:
            dict[keys].append(line)
with open (IDlist, "r") as IDlist:
	for n in IDlist:
		IDs = n.strip().replace(">","")
		Outfile.write('>' +str(IDs) + '\n' + str(''.join(dict[IDs])) + '\n')

ref.close()
IDlist.close()
Outfile.close()
