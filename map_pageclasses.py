#%%
import os
import pagexml
import glob
#%%
validated_files = glob.glob("/home/waqas/repos/platform-client/platform_client/merged_train/*")

for el in validated_files:
    name = os.path.basename(el)
    file_ocr = os.path.join('/home/waqas/repos/platform-client/platform_client/merged_train/',name,name+"_ocr"+".xml")
    ocr = pagexml.PageXML(file_ocr)
    
    file_val = os.path.join('/home/waqas/repos/platform-client/platform_client/merged_train/',name,name+"_validated"+".xml")
    val = pagexml.PageXML(file_val)
    
    for i, page in enumerate(ocr.select('//_:Page')):
        classes = val.getPropertyValue(val.selectNth('//_:Page', i), 'class')
        # if classes == "":
            # val.setProperty(val.selectNth('//_:Page', i), 'class', 'c6M0z1PY-echo-4sVD-5g9o-fZhiyiOZajpF')
            # val.write(file_val)
            
        ocr.setProperty(ocr.selectNth('//_:Page', i), 'class', classes)
        try:
            ocr.write(file_ocr)
        except Exception as e:
            print(e)
# %%

