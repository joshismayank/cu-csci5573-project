import os
import tempfile
from io import BytesIO
from PIL import Image
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
    """ Parses a 'multipart/form-data' upload request
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
         Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """

    # This code will process each non-file field in the form
    #fields = {}
    #data = request.form.to_dict()
    #for field in data:
    #    fields[field] = data[field]
    #    print('Processed field: %s' % field)

    # This code will process each file uploaded
    files = request.files.to_dict()
    for file_name, file in files.items():
        print(type(file))
        file.save(get_file_path(file_name))
        img = cv2.imread(get_file_path(file_name))
        height, width, channels = img.shape
        response = {
            'width' : width,
            'height' : height
            }
       	response_pickled = json.dumps(response)
    return response_pickled

    # Clear temporary directory
    for file_name in files:
        file_path = get_file_path(file_name)
        os.remove(file_path)

    return 
