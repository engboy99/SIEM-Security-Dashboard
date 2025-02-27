from elasticsearch import Elasticsearch

def send_to_elk(log_data):
    es = Elasticsearch(["http://localhost:9200"])
    es.index(index="logs", body=log_data)
