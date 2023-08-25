import json
from datetime import datetime

from elasticsearch import Elasticsearch

from situation.es import tsec_audit_data_print

es = Elasticsearch(
    [
        {"host": "192.168.244.128", "port": 9200, 'scheme': "http"},
    ],
    http_auth=("security", "s2u1p3e4r"),
    request_timeout=3600
)


def generate_sample_dataset():
    dataset = []
    data = tsec_audit_data_print.generate_test_data()
    dataset.append(data)
    return dataset


# Generate a sample dataset with 10 records
sample_dataset = generate_sample_dataset()

# Print the generated dataset as JSON
print(json.dumps(sample_dataset, indent=4, ensure_ascii=False))


# 将样本数据集索引到Elasticsearch中
def index_sample_dataset(dataset, index_name):
    for i, data in enumerate(dataset):
        es.index(index=index_name, body=data, id=data["computer_guid"])


# 将样本数据集索引到Elasticsearch中，使用索引名称'tsec-computer'
index_sample_dataset(sample_dataset, f"tsec-audit-data-print-{datetime.now().strftime('%Y-%m')}")
