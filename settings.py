import datetime

CollectionsSize = 100
url = "mongodb://root:root@mongodb:27017/"
DBName = "BocksDB"
CollectionName = "Books"
authors_count_min = 1
authors_count_max = 30
startdate = datetime.datetime(2019, 1, 1, 0, 0)
pipeline_top10authors = [
    {"$group": {
        "_id": {"author": "$author"},
        "countText": {"$count": {}}
    }
    },
    {
        "$limit": 10
    },
    {
        "$addFields":
            {
                "author": "$_id.author"
            }
    },
    {
        "$sort":
            {
                "countText": -1
            }
    },
    {
        "$project": {"_id": 0, "author": 1, "countText": 1}
    }
]


def pipeline_histogram(start, today):
    pipeline_endpoint2 = [
        {
            "$match": {
                "date": {
                    "$gte": start, "$lt": today
                }
            }
        },
        {"$group": {
            "_id":
                {
                    "year": {"$year": "$date"},
                    "month": {"$month": "$date"}
                },
            "count": {"$sum": 1}
        }
        },
        {
            "$addFields": {
                "year": "$_id.year",
                "month": "$_id.month"
            }
        },
        {
            "$sort":
                {
                    "year": 1,
                    "month": 1
                }
        },
        {
            "$project": {"_id": 0, "year": 1, "month": 1, "count": 1}
        }
    ]

    return pipeline_endpoint2
