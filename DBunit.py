import pymongo
import datetime
import lorem
import names
import random
import settings
import assistive


def MongoConnector():
    url = settings.url
    client = pymongo.MongoClient(url)

    db = client[settings.DBName]
    main_collection = db[settings.CollectionName]
    return main_collection


def clearDB(collection, selection={}):
    collection.delete_many(selection)


def fillDB(collection=None, size=settings.CollectionsSize):
    NamesSum = random.randint(settings.authors_count_min, settings.authors_count_max)

    namesColl = []

    i = 0
    while i < NamesSum:
        i += 1
        namesColl.append(names.get_full_name())

    Docs = []
    i = 1
    while i <= size:
        name = namesColl[random.randint(0, NamesSum - 1)]
        paragraph = lorem.paragraph()
        date = assistive.getrndmdate()

        doc = {
            "author": name,
            "paragraph": paragraph,
            "date": date
        }

        Docs.append(doc)

        i += 1

    collection.insert_many(Docs)


def Get_Data(collection=None, selection={}):
    if collection is None:
        collection = MongoConnector()

    result = collection.find(selection)
    return result


def Get_top10authors(collection=None):
    if collection is None:
        collection = MongoConnector()

    pipeline = settings.pipeline_top10authors
    result = collection.aggregate(pipeline)

    return result


def Get_histogram(collection=None):
    if collection is None:
        collection = MongoConnector()

    start = settings.startdate
    today = datetime.datetime.today()
    pipeline = settings.pipeline_histogram(start, today)
    result = collection.aggregate(pipeline)

    return result
