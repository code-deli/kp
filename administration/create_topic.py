from confluent_kafka.admin import AdminClient,NewTopic


if __name__ == '__main__':
    config = {
        'bootstrap.servers' : 'localhost:9092',
        'client.id': 'my-client'
    }
    client = AdminClient(config)
    newTopic = NewTopic('topic',num_partitions=1,replication_factor=1)
    res = client.create_topics([newTopic])
    print('---New Created Topics---')
    for key, val in res.items():
        try:
            val.result()
            print('topic name : {tn}'.format(tn=key))
        except Exception as e:
            print("failed to create new topic {}: {}".format(key, e))
