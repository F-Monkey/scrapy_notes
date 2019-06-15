from tornado.web import RequestHandler

from spider.io.DB import session
from spider.io.pojo import User


class WordsHandler(RequestHandler):
    
    def get(self, *args:str, **kwargs:str)->None:
        RequestHandler.get(self, *args, **kwargs)
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)

class UserHandler(RequestHandler):
    def get(self, *args:str, **kwargs:str)->None:
        return session.query(User)  # @UndefinedVariable

    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)

class ImageHandler(RequestHandler):
    def get(self, *args:str, **kwargs:str)->None:
        RequestHandler.get(self, *args, **kwargs)
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)