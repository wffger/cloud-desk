import botocore
from boto3 import resource
from settings.config import env

dynamodb = resource(
    "dynamodb",
    region_name=env.AWS_REGION_NAME,
    aws_access_key_id=env.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
)

tables = [
    {
        "TableName": "Song",
        "AttributeDefinitions": [
            {"AttributeName": "LoaderId", "AttributeType": "S"},
            {"AttributeName": "SongId", "AttributeType": "S"},
        ],
        "KeySchema": [
            {"AttributeName": "LoaderId", "KeyType": "HASH"},
            {"AttributeName": "SongId", "KeyType": "RANGE"},
        ],
        "ProvisionedThroughput": {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        },
    },
]


def create_tables(name: str | None):
    try:
        if name:
            table = [v for i, v in enumerate(tables) if v['TableName'] == name][0]
            print(type(table))
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                ProvisionedThroughput=table["ProvisionedThroughput"]
            )
        else:
            for table in tables:
                dynamodb.create_table(
                    TableName=table["TableName"],
                    KeySchema=table["KeySchema"],
                    AttributeDefinitions=table["AttributeDefinitions"],
                    ProvisionedThroughput=table["ProvisionedThroughput"],
                    # BillingMode="PAY_PER_REQUEST"
                )
    except botocore.exceptions.ClientError as error:
        # Put your error handling logic here
        return error
        raise error
    except botocore.exceptions.ParamValidationError as error:
        raise ValueError(f'The parameters you provided are incorrect: {error}')
