import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('QlVRYgcvK88ksTpI1rkPnxIMWRsgvD2Xei7uCFSLkVg')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def emotion_analysis(self,text):
        response = paralleldots.emotion(text)
        return response

