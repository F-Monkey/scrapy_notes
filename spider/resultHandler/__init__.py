from tornado.web import RequestHandler



class wordsHandler(RequestHandler):
    
    def get(self, *args:str, **kwargs:str)->None:
        RequestHandler.get(self, *args, **kwargs)
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)