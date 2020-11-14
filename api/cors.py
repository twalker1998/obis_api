class CorsMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def process_response(self, req, resp):
		resp["Access-Control-Allow-Headers"] = "*"
		resp["Access-Control-Allow-Methods"] = "*"
		return resp
