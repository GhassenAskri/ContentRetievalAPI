# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyDH3iz9Xmr0e2exFsL4ithP3dbWI4vGdL4"
# API client

def get_data(keyword):
    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
    # 'request' variable is the only thing you must change
    # depending on the resource and method you need to use
    # in your query
    request = youtube.search().list( part="snippet", maxResults=5, q=keyword, relevanceLanguage = "ar", publishedAfter ="2011-01-13T00:00:00Z", publishedBefore ="2011-01-14T00:00:00Z")
    # Query execution
    response = request.execute()
# Print the results
print(response)