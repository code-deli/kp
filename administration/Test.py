from confluent_kafka.admin import AdminClient,ClusterMetadata,TopicMetadata,ConfigResource,ConfigEntry
from typing import Dict





if __name__ == '__main__':

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














