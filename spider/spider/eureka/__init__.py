from py_eureka_client import eureka_client
import tornado
from tornado.web import RequestHandler

client_port = 7070
app_name = "spider"
eureka_server = 'http://127.0.0.1:1111/eureka'
instance_port = client_port


def regist():
    eureka_client.init(eureka_server=eureka_server, app_name=app_name, instance_port=instance_port)
    handlers = []
    app = tornado.web.Application(handlers=handlers)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(client_port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    regist()
