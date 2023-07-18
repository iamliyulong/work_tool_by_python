import json

from elasticsearch import Elasticsearch

from situation.es import tsec_computer

es = Elasticsearch(
    [
        {"host": "10.66.77.35", "port": 9200, 'scheme': "http"},
    ],
    http_auth=("security", "s2u1p3e4r"),
    request_timeout=3600
)


# Generate a sample dataset with n number of records
# def generate_sample_dataset(n):
#     dataset = []
#     for i in range(1, n + 1):
#         data = generate_test_data(i)
#         dataset.append(data)
#     return dataset

def generate_sample_dataset(computer_guid):
    dataset = []
    data = tsec_computer.generate_test_data(computer_guid)
    dataset.append(data)
    return dataset


# Generate a sample dataset with 10 records
sample_dataset = generate_sample_dataset("2023062801")

# Print the generated dataset as JSON
print(json.dumps(sample_dataset, indent=4, ensure_ascii=False))


# 将样本数据集索引到Elasticsearch中
def index_sample_dataset(dataset, index_name):
    for i, data in enumerate(dataset):
        es.index(index=index_name, body=data, id=data["computer_guid"])


# 将样本数据集索引到Elasticsearch中，使用索引名称'tsec-computer'
index_sample_dataset(sample_dataset, 'tsec-computer')
