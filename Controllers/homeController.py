class homeController():
        routeprefix = "/home"
        def GET(self, request):
            response = "<html><body>I am homeController.<br/>"
            response += "My Uri is: %s<br/>" % (request.uri)
            response += "My Method is: %s<br/>" % (request.method)
            response += "My URLPath is: %s<br/>" % (request.URLPath)
            response += "<hr/>"
            response += "All the nitty gritty:<br/> %s" % (dir(request))
            response += "</body></html>"
            return response
        def POST(self, request):
            return render_GET(self, request)

        GET.route = ["/","/home"]
