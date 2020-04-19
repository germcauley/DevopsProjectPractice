import boto3

dynamo_client = boto3.client('dynamodb', region_name='eu-west-1')


def get_items():
    return dynamo_client.scan(
        TableName='MessageBoard'
    )


def put_items(name,message):
    dynamo_client.put_item(
        TableName='MessageBoard',
        Item={
            'User':{'S': name},
            'Comments':{'S':message}
            }
    )

def delete_item(name,message):
      dynamo_client.delete_item(
        TableName='MessageBoard',
        Item={
            'User':{'S': name},
            'Comments':{'S':message}
            }
    )

