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
      change configuration of the topic - retention period example
    """
    config: Dict = {
        'bootstrap.servers':'localhost:9092'
    }

    admin_client: AdminClient = AdminClient(config)
    clusterMetadata: ClusterMetadata = admin_client.list_topics()
    topics: Dict[str,TopicMetadata] = clusterMetadata.topics
    topic = {k:v for k,v in topics.items() if k == 'mytopic'}
    topicMetaData : TopicMetadata = topic.get('mytopic')
    print(topicMetaData.partitions)

    configResource:ConfigResource = ConfigResource(ConfigResource.Type.TOPIC,'mytopic')
    res = admin_client.describe_configs([configResource])
    val = list(res.values())
    existing_config: dict = val[0].result()
    print(existing_config)
    newConfig = { 'retention.ms':'304800000' }
    configResource: ConfigResource = ConfigResource(ConfigResource.Type.TOPIC, 'mytopic',set_config=newConfig)
    admin_client.alter_configs([configResource])

    """
      next adevnture goes here
    """










