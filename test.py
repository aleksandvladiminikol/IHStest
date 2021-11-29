import DBunit
import datetime
import assistive
import api


def start():
    start = datetime.datetime.now()

    collection = DBunit.MongoConnector()
    DBunit.clearDB(collection)
    DBunit.fillDB(collection)

    top10 = DBunit.Get_top10authors()
    histogram = DBunit.Get_histogram()

    end1 = datetime.datetime.now()
    print(end1 - start)

    assistive.readResult(top10)
    assistive.readResult(histogram)

    end2 = datetime.datetime.now()
    print(end2 - end1)
