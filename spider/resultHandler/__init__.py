from tornado.web import RequestHandler

from spider.io.DB import session
from spider.io.pojo import User
import pyrestful
from pyrestful.rest import get


class WordsHandler(pyrestful.rest.RestHandler):
    
    @get(_path='/contents')
    def get(self, *args:str, **kwargs:str)->None:
        RequestHandler.get(self, *args, **kwargs)
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)

class UserHandler(pyrestful.rest.RestHandler):
    
    def get(self, *args:str, **kwargs:str)->None:
        return session.query(User)  # @UndefinedVariable

    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)

class ImageHandler(pyrestful.rest.RestHandler):
    def get(self, *args:str, **kwargs:str)->None:
        RequestHandler.get(self, *args, **kwargs)
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)