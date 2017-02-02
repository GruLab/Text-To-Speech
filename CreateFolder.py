import os

root_dir = os.getcwd()
subfolders = ('\COMP', '\DO', '\LANG_SPEC', '\MOS', '\MRT', '\OMOS', '\SUS')
i = 0
for folder in subfolders:
	os.makedirs(root_dir + '\Input\\' + subfolders[i])
	os.makedirs(root_dir + '\Output\\' + subfolders[i])
	i += 1
