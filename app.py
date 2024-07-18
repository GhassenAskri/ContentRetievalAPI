from urllib import response
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
# API client library
import googleapiclient.discovery

app = Flask(__name__)

api = Api(app, version='1.0', title='VideoClassifier API',
          description='description',)

ns = api.namespace('VideoClassifier', description='VideoClassifier operations')

keyword_model = api.model('keyworld_model', {
    'keyword': fields.String(required=True, description='search_keyworld'),
    'publishedAfter': fields.String(required=False, description='format example : 2011-01-13T00:00:00Z'),
    'publishedBefore': fields.String(required=False, description='format example : 2011-01-13T00:00:00Z')
})

keyword_list_model = api.model('keyworld_list_model', {
    'keywords': fields.List(fields.Nested(keyword_model))
})

# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "<your-youtube-developer-key>"

def create_url(content):
    res =[]
    for item in content:
        res.append({'url':'https://www.youtube.com/watch?v='+item['id']['videoId']})
    return res

@ns.route('/data')
class DataCollector(Resource):
    @ns.doc('Get DATA')
    @ns.expect(keyword_list_model)
    def post(self):
        response = get_data(api.payload['keywords'][0]['keyword'],api.payload['keywords'][0]['publishedAfter'],api.payload['keywords'][0]['publishedBefore'])
        res = create_url(response['items'])
        return jsonify(res)


def get_data(keyword,publishedAfter, publishedBefore):
    # API client
    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
    # 'request' variable is the only thing you must change
    # depending on the resource and method you need to use
    # in your query
    request = youtube.search().list( part="snippet",relevanceLanguage = "ar",  maxResults=10, q=keyword, publishedAfter = publishedAfter, publishedBefore =publishedBefore)
    # Query execution
    response = request.execute()
    # Print the results
    return(response)

if __name__ == '__main__':
    app.run(debug=True)