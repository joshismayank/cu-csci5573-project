def handle(req):
	"""
	import os
	import tempfile
	from io import BytesIO
	import cv2
	import json
	from werkzeug.utils import secure_filename

	# Helper function that computes the filepath to save files to
	def get_file_path(filename):
    		# Note: tempfile.gettempdir() points to an in-memory file system	
		# on GCF. Thus, any files in it must fit in the instance's memory.
		file_name = secure_filename(filename)
		return os.path.join(tempfile.gettempdir(), file_name)

	
	def parse_multipart(request):	
		files = request.files.to_dict()
		for file_name, file in files.items():
			file.save(get_file_path(file_name))
			img = cv2.imread(get_file_path(file_name))
			height, width, channels = img.shape
			response = {
			'width' : width,
			'height' : height
			}
			response_pickled = json.dumps(response)
		return response_pickled
	
		for file_name in files:
			file_path = get_file_path(file_name)
			os.remove(file_path)
		return
	"""
	fibon = []
	def fibo(n):
		if n <= 1:
			return n
		else:
			return(fibo(n-1) + fibo(n-2))

	for i in range(int(req)):
		fibon.append(fibo(i))
	response = {}
	i = 0;
	for l in fibon:
		response[i] = l
		i += 1
	return fibon

