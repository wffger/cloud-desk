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
    },
]

print([v for i, v in enumerate(tables) if v['TableName'] == 'Song'])


next(item for item in tables if item["TableName"] == "Song")