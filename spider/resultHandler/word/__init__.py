from spider.io.DB import session
from spider.io.pojo import User

def anlysisUser(url):
    pass

def queryUsers(*args):
    return session.query(User)  # @UndefinedVariable
    