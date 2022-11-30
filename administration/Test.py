from confluent_kafka.admin import AdminClient,ClusterMetadata,TopicMetadata
from typing import Dict





if __name__ == '__main__':

    config: Dict = {
        'bootstrap.servers':'localhost:9092'
    }

    admin_client: AdminClient = AdminClient(config)
    clusterMetadata: ClusterMetadata = admin_client.list_topics()
    topics: Dict[str,TopicMetadata] = clusterMetadata.topics
    print({k:v for k,v in topics.items() if k=='topic'})









