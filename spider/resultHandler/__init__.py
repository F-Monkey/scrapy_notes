from tornado.web import RequestHandler

from spider.io.DB import session
from spider.io.pojo import User
import pyrestful
from pyrestful.rest import get,post,delete
from resultHandler.word import ContentProcessor
import socket

user_content_dict = {}

class WordsHandler(pyrestful.rest.RestHandler):
    
    @get(_path='/contents/{userUrl}')
    def get(self, userUrl)->None:
        cp = ContentProcessor(userUrl)
        return cp.analisysUserContent()
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)

class UserHandler(pyrestful.rest.RestHandler):
    
    def get(self, *args:str, **kwargs:str)->None:
        return session.query(User)  # @UndefinedVariable

    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)

class ImageHandler(pyrestful.rest.RestHandler):
    @get(_path='/worldCloud/gen/{userUrl}')
    def get(self, *args:str, **kwargs:str)->None:
        pass
    
    def post(self, *args:str, **kwargs:str)->None:
        RequestHandler.post(self, *args, **kwargs)