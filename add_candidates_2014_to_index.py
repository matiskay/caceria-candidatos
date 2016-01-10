from elasticsearch import Elasticsearch
from tqdm import tqdm


es = Elasticsearch()

with open("data/prosecuted_candidates_2014.tsv", "r") as handle:
    data = handle.readlines()

for raw_line in tqdm(data):
    line = raw_line.strip()
    candidate = line.split("\t")
    doc = {
        "raw_data": ', '.join([
            candidate[2],
            candidate[3],
            candidate[4],
            candidate[1],
            candidate[7],
        ]),
        "source": "candidato_2014",
    }

    res = es.index(index="great_db", doc_type="text", body=doc)
