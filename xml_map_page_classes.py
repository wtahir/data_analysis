#%%
import os
import pagexml
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import json
#%%
validated_files = glob.glob("/home/waqas/repos/nlp_classification/aza_doc-class-test/*")

f = open('doc_class.json')
data = json.load(f)

for el in validated_files:
    name = os.path.basename(el)
    file_ocr = os.path.join('/home/waqas/repos/nlp_classification/aza_doc-class-test/', name)
    ocr = pagexml.PageXML(file_ocr)
    
#     # file_val = os.path.join('/home/waqas/repos/nlp_classification/aza_doc-class-test/',"_validated"+".xml")
#     # val = pagexml.PageXML(file_val)
    
    for i, page in enumerate(ocr.select('//_:Page')):
        class_ = ocr.getPropertyValue(ocr.selectNth('//_:Page', i), 'class')
        for j in data['pageClasses']:
            if class_ == j['id']:
#             # val.setProperty(val.selectNth('//_:Page', i), 'class', 'c6M0z1PY-echo-4sVD-5g9o-fZhiyiOZajpF')
#             # val.write(file_val)         
                ocr.setProperty(ocr.selectNth('//_:Page', i), 'class', j['name'])
                try:
                    ocr.write(file_ocr)
                except Exception as e:
                    print(e)
# %%

# for el in validated_files:
#     name = os.path.basename(el)
#     file_ocr = os.path.join('/home/waqas/repos/nlp_classification/aza_doc-class-test/', name)
#     ocr = pagexml.PageXML(file_ocr)

#     for i, page in enumerate(ocr.select('//_:Page')):
#         class_ = ocr.getPropertyValue(ocr.selectNth('//_:Page', i), 'class')
#         node = ocr.selectNth('//_:Page/@imageFilename', i)
#         image_ = ocr.getValue(node)
#         class_ = ocr.getPropertyValue(ocr.selectNth('//_:Page', i), 'class')
#         if class_ == 'cost_check' or class_ == 'expert_report':
#             print(file_ocr, image_)
