import boto3

dynamo_client = boto3.client('dynamodb', region_name='eu-west-1')


def get_items():
    return dynamo_client.scan(
        TableName='YourTestTable'
    )


def put_items():
    dynamo_client.put_item(
        TableName='YourTestTable',
        Item={
            'Artist':{'S': "Bach"},
            'SongTitle':{'S':'Goldberg Variations'}
            } 
    )
    
