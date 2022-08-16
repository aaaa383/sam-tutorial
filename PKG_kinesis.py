import json
import random
import time
import datetime
import boto3

def main():

    # 以下の５つの変数を環境に合わせて変更する
    accesskey = 'AKIAUCL276CXSVMAQ5F2'
    secretkey = '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'
    region = 'ap-northeast-1'
    stream_name = 'test_user2'
    uuid = 'test03'

    client = boto3.client("firehose", aws_access_key_id=accesskey, aws_secret_access_key=secretkey, region_name=region)

    count = 0
    while count < 100 :

        stream_data = {
                'uuid': uuid,
                'car_count': random.randrange(0,5),
                'timestamp': "{0:%Y-%m-%dT%H:%M:%SZ}".format(datetime.datetime.now())
            }

        response = client.put_record(
            DeliveryStreamName=stream_name,
            Record={
            'Data': json.dumps(stream_data)
            }
        )

        print(json.dumps(stream_data))
        print(response)
        count += 1
        time.sleep(1)


if __name__ == '__main__':
  main()