from flask import Flask, render_template
import DBunit

app = Flask(__name__)


@app.route('/', methods=['GET'])
def loadDB():
    _items = DBunit.Get_Data()
    result = [item for item in _items]
    return render_template('maintable.html', items=result)


@app.route('/statistic', methods=['GET'])
def statistic():
    top10authors = response_top10authors()
    histogram = response_histogram()

    return top10authors + histogram


def response_top10authors():
    _items = DBunit.Get_top10authors()
    result = [item for item in _items]
    return render_template('top10authors.html', items=result)


def response_histogram():
    _items = DBunit.Get_histogram()
    result = [item for item in _items]
    return render_template('histogram.html', items=result)


if __name__ == '__main__':
    collection = DBunit.MongoConnector()
    DBunit.clearDB(collection)
    DBunit.fillDB(collection)

    app.run(host='0.0.0.0', debug=False)
