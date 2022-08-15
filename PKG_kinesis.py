import json
import random
import time
import datetime
import boto3

def main():

    # 以下の５つの変数を環境に合わせて変更する
    accesskey = 'AKIATS576XQZB6VJJ57Q'
    secretkey = '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'
    region = 'ap-northeast-1'
    stream_name = 'test_user'
    uuid = 'test01'

    client = boto3.client("firehose", aws_access_key_id=accesskey, aws_secret_access_key=secretkey, region_name=region)

    count = 0
    while count < 10 :

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