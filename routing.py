#from twisted.web.resource import Resource

class MyRouter(Resource)
    def __init__(self):
        #Resource.__init__(self)
        #self.isLeaf = True # We shall handle all requests coming to a controller
        self.routeMap = {}


    def loadStaticFileRoutes():
        """
        Add your static File routes here using: self.putChild('path','folder')
        """

    def loadAttributeRouting():
        """
        Loops over the Controllers folder specified in the config and loads the attributes.
        Add a 'route' attribute to your Controller methods if you want to use Attribute Routing.
        You can also add a 'method' attribute to specify which HTTP Method you want to use.
        """
        pass

    def loadCustomRoutes():
        """
        Any custom routes you wish to add go here. These will take precedence over other rules.
        """
        pass

    # Don't touch this method!
    def loadRoutes(self):
        loadStaticFileRoutes()
        loadCustomRoutes()
        loadAttributeRouting()

"""
    def getController(self,uri):
        "Determine which controller to run"
        controller = None
        if(request.uri == '/'):
            controller = 'homeController'
        else:
            controller = request.uri.split('/')[1] + 'Controller'
        return controller
"""
