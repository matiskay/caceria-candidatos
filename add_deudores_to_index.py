"""Add deudores al Estado to index"""
import sys

from elasticsearch import Elasticsearch
from tqdm import tqdm


if len(sys.argv) < 2:
    print("Enter input file as argument")
    sys.exit(1)

input_file = sys.argv[1].strip()

es = Elasticsearch()

with open(input_file, "r") as handle:
    data = handle.readlines()

for raw_line in tqdm(data):
    line = raw_line.strip()
    fields = line.split("\t")
    doc = {
        "raw_data": " ".join([fields[2], fields[10], fields[1]]),
        "source": "deudores",
    }

    res = es.index(index="great_db", doc_type="text", body=doc)
