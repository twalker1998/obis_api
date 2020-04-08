class CorsMiddleware(object):
	def process_response(self, req, resp):
		resp["Access-Control-Allow-Headers"] = "*"
		resp["Access-Control-Allow-Methods"] = "*"
		return resp
