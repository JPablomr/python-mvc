# Controller Spec

Controllers are implemented as classes/files ending on 'Controller'.
This convention **must** be followed for the router to recognize the controllers.

Controllers have a form of attribute-based routing (a la .net's attribute routing).
This is accomplished with function and class variables.

Methods will only receive a request object which contains the info of the request.

Every method in a controller that we want to handle a url must contain the following variables:

- route: One or more routes to bind this method to.

  ```python
  showHome.route = ["","home"]
  ```

There are also these optional fields:

- method: One or more HTTP methods that the function can function listen to. Will be GET by default.
