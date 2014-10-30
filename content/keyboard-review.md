Title: My First Review
Date: 2010-12-03 10:20
Category: Review
Tags:test,kk

### Following is a review of my favorite mechanical keyboard.

	:::python
	def rebuild():
	    clean()
	    build()

	def regenerate():
	    local('pelican -r -s pelicanconf.py')

	def serve():
	    os.chdir(env.deploy_path)

	    PORT = 8000
	    class AddressReuseTCPServer(SocketServer.TCPServer):
	        allow_reuse_address = True

	    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

	    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
	    server.serve_forever()

	def reserve():
	    build()
	    serve()

	def preview():
	    local('pelican -s publishconf.py')
