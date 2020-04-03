class CorsMiddleware(object):
	def process_response(self, req, resp):
		resp["Access-Control-Allow-Headers"] = "*"
		resp["Access-Control-Allow-Methods"] = "*"
		resp["Access-Control-Allow-Origin"] = "*"
		return resp
