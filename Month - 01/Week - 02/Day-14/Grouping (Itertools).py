'''
DEEP DIVE: 14.9 Capstone: Grouping (Itertools)
Goal: Group list of dicts by "category". 
Deep Dive: Use itertools.groupby. Note: Data MUST be sorted by the key 
first!
'''

from itertools import groupby
from operator import itemgetter

def group_by_category(data):
    # step 1: sort by category
    data = sorted(data, key=itemgetter("category"))

    # step 2: group
    grouped = {}
    for key, group in groupby(data, key=itemgetter("category")):
        grouped[key] = list(group)

    return grouped
