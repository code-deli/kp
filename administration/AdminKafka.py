from confluent_kafka.admin import *
from typing import Dict



if __name__ == '__main__':
    config = {
        'bootstrap.servers' : 'localhost:9091',
        'client.id' : 'my-client'
    }

    """
    1. create config 
    2. list all topics 
    3. for every topic list its parititons
    4. also list the replicas for every partition
    5. find out which brokers are holding those topics and its partitions
    """
    adminclient: AdminClient = AdminClient(conf=config)
    metadata: ClusterMetadata = adminclient.list_topics()
    topics: Dict = metadata.topics
    print(f'Number of topics :{topics.keys()}')
    for key , value in topics.items():
        print(f'Name:{key} -> ')
        topicmetadata: TopicMetadata = value
        partitions:Dict = topicmetadata.partitions
        for key,value in partitions.items():
            print(key,len(value.replicas))


    brokers: Dict = metadata.brokers
    for key, value in brokers.items():
        print(f'Broker:{key} -> {value}')


    """
      next adevnture goes here
    """










