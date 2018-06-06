from twisted.web.resource import Resource

class loginController(Resource):
        def __init__(self):
            Resource.__init__(self)
            self.isLeaf = True
        def render_GET(self, request):
            return "<html><body>I am loginController. My Uri is: %s</body></html>" % (request.uri)
        def render_POST(self, request):
            return render_GET(self, request)

        render_GET.route='login'
