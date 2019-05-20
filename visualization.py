#%%
from PIL import Image,ImageDraw,ImageFont
import json
import sys

#%%


#%%
args = sys.argv
print(args)
if len(args) == 4:
    print('provided')
    in_file = args[1]
    json_file = args[2]
    out_file = args[3]
else:
    print('default')
    in_file = 'bas1/data/img/Schadenbild80654712030674810.jpg'
    json_file = 'bas1/open_alpr_results_comVersion/Schadenbild80654712030674810.jpg.json'
    out_file = 'bas1/output/Schadenbild80654712030674810.jpg'
debug = False

#%%
img = Image.open(in_file)
if debug:
    img.show()

#%%
with open(json_file, 'rb') as f:
    data = json.load(f)
for result in data['results']:

    #%%
    def parse_result(result):
        coordinates = result['coordinates']
        points = []
        for coordinate in coordinates:
            points.append((coordinate['x'], coordinate['y']))
        plate = {}
        plate['polygon'] = points
        plate['text'] = result['plate']
        plate['confidence'] = result['confidence']
        return plate
    result = parse_result(result)
    result

    #%%
    #def draw_plate(img, result):
    font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf', size=50)
    draw = ImageDraw.Draw(img)
    polygon = result['polygon']
    draw.polygon(polygon,fill=None, outline='cyan')
    text = result['text']
    draw.textsize(text, font)
    draw.text(result['polygon'][3],result['text'], fill='cyan', font=font)
    #draw.text(result['polygon'][2],str(result['confidence']), fill='green')
    #return img
    #img = draw_result(img, plate)
if debug:
    img.show()

#%%
img.save(out_file)
