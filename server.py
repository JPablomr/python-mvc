from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.static import File


class Router(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.putChild("js", File("./scripts/js"))
        self.putChild("css", File("./scripts/css"))

    def getChild(self,path,request):
        controller = None
        if(request.uri == '/'):
            controller = 'homeController'
        else:
            controller = request.uri.split('/')[1] + 'Controller'
        print(controller)
        return getattr(getattr(Controllers,controller),controller)()

def StartServer():
    factory = Site(IController())
    reactor.listenTCP(8080, factory)
    reactor.run()


if __name__ == '__main__':
    execfile('__init__.py')
    StartServer()
