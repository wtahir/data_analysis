import os
import pagexml
import glob

doc_dir = 'fed90951-622d-47cb-957d-fe95b2addb3'
print(doc_dir)
xml_file = os.path.join(doc_dir, 'page.xml')
pxml = pagexml.PageXML(xml_file)

page_list = pxml.select('//_:Page')
for p, page in enumerate(page_list):
    width = pxml.getPageWidth(page)
    height = pxml.getPageHeight(page)

    img_file = 'image_%d.jpeg' % p

    pxml.setPageImageFilename(page, img_file)

    #cmd = 'mogrify -resize %dx%d %s' % (width, height, img_file)
    cmd = 'mogrify -resize {}x{} {}'.format(width, height, os.path.join(doc_dir, img_file))

    print(cmd)
    os.system(cmd)
# pxml.write(xml_file)