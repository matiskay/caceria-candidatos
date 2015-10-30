"""Adds all data of "deudores al Estado" to our elasticsearch index.
"""
from elasticsearch import Elasticsearch


es = Elasticsearch()

with open("BASE_DE_DATOS_REGISTRO_DE_DEUDORES_POR_DELITO_AGRAVIO_ESTADO.CSV", "r") as handle:
    data = handle.readlines()

for raw_line in data:
    line = raw_line.strip()
    fields = line.split("\t")
    doc = {
        "raw_data": " ".join([fields[2], fields[10], fields[1]]),
        "source": "deudores",
    }

    res = es.index(index="great_db", doc_type="text", body=doc)
    print("created: {}".format(res['created']))
