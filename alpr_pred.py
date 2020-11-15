import base64
import requests
import glob
import os
import json


# def predictions_json(image_path, secret_key):
#     for i in glob.glob('*.jpg'):
#         with open(image_path, 'rb') as image_file:
#             img_base64 = base64.b64encode(image_file.read())
#         url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=eu&secret_key=%s' % (secret_key)
#         r = requests.post(url, data = img_base64)
#         pred = json.dumps(r.json(), indent=2)
#     return print(pred)

def predictions_json(image_path, secret_key):
    for i in glob.glob('test/*.jpg'):
        with open(i, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())
            url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=eu&secret_key=%s' % (secret_key)
            r = requests.post(url, data = img_base64)
            json_file = i.replace('.jpg', '.json')
            with open(json_file, 'w') as outfile:  
                json.dump(r.json(), outfile)
            return

# end
