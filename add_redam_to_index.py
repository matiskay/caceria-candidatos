"""Adds all data of "REDAM" to our elasticsearch index.
"""
from elasticsearch import Elasticsearch


es = Elasticsearch()

with open("todos_deudores_REDAM.tsv", "r") as handle:
    data = handle.readlines()

for raw_line in data:
    line = raw_line.strip()
    debtor = line.split("\t")
    doc = {
        "raw_data": ', '.join(debtor),
        "source": "redam",
    }

    res = es.index(index="great_db", doc_type="text", body=doc)
    print("created: {}".format(res['created']))
