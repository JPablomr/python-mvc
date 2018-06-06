from twisted.web.resource import Resource
import Controllers
#
# IController will:
#  - Resolve which controller to use (He'll get the controllers from the Controllers folder)

class IController(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.isLeaf = True # We shall handle all requests coming to a controller

    def getController(self,uri):
        "Determine which controller to run"
        controller = None
        if(uri == '/'):
            controller = 'homeController'
        else:
            controller = uri.split('/')[1] + 'Controller'
        return controller

    def render_GET(self, request):
        controllerToHandle = self.getController(request.uri)
        #return "<html><body>I am homeController. My Uri is: %s</body></html>" % (request.uri)
        return getattr(getattr(Controllers,controllerToHandle),controllerToHandle)().GET(request)
        pass
    def render_POST(self, request):
        return render_GET(self, request)
