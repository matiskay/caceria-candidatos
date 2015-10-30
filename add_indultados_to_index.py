"""Adds all data of "narcoindultados" to our elasticsearch index.
"""
from elasticsearch import Elasticsearch


es = Elasticsearch()

with open("conmutados_cleaned.txt", "r") as handle:
    data = handle.readlines()

for raw_line in data:
    line = raw_line.strip()
    doc = {
        "raw_data": line,
        "source": "narcoindultos",
    }

    res = es.index(index="great_db", doc_type="text", body=doc)
    print("created: {}".format(res['created']))
