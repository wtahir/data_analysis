#%%
import pagexml
import glob
import os
import shutil
# %%
train_files = [el for el in os.listdir("/home/waqas/repos/platform-client/platform_client/aza_doc-class-train/")]

validated_files = [el for el in os.listdir("/home/waqas/repos/platform-client/platform_client/aza_doc-class-train-validated/")]

for el in train_files:
    path = os.path.join("/home/waqas/repos/platform-client/platform_client/merged_train", el.split(".")[0])
    os.makedirs(path, exist_ok=True)

for el in validated_files:
    name = el.split(".")[0]
    src = os.path.join('/home/waqas/repos/platform-client/platform_client/aza_doc-class-train',el)
    dest = os.path.join("/home/waqas/repos/platform-client/platform_client/merged_train", name, name+"_ocr"+".xml")
    shutil.copy(src, dest)
    
    src = os.path.join("/home/waqas/repos/platform-client/platform_client/aza_doc-class-train-validated", el)
    dest = os.path.join("/home/waqas/repos/platform-client/platform_client/merged_train", name, name+"_validated"+".xml")
    shutil.copy(src, dest)
# %%
