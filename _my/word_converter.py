import pypandoc
import os
import pandoc


# if getattr(sys, 'frozen', False):
#     # If the application is run as a bundle, the PyInstaller bootloader
#     # extends the sys module by a flag frozen=True and sets the app 
#     # path into variable _MEIPASS'.
#     path = sys._MEIPASS
# else:
#     path = os.path.dirname(os.path.abspath(__file__))
path = os.getcwd()

print(path)

from pypandoc.pandoc_download import download_pandoc
# see the documentation how to customize the installation path
# but be aware that you then need to include it in the `PATH`
download_pandoc()


# import textwrap3

def converter(file):
    file = pypandoc.convert_file(file, 'plain', outputfile=(file[0:-5]+'.txt'), extra_args=['--wrap=auto']) 




file_list = os.listdir(path+'/')

print(file_list)

for file in file_list:
    if file[-4:] == 'docx':
        print('found:    ', file)
        converter(path+'/'+file)
        print('converted:', file)

os.system('pause')

# file_list = os.listdir(path+'/')

# print(file_list)

# for file in file_list:
#     if file[-3:] == 'txt':
#         print('slicing txt:     ', file)
#         with open(file, "w+",encoding='utf-8') as text_file:
#             new_text_file = []
#             text_as_lines = text_file.readlines()
#             for line in text_as_lines:
#                 wrapped_line = textwrap3.fill(line, width=30)
#                 new_text_file.append(wrapped_line)
#             text_file.write("\n".join(new_text_file))    
#         print('slicing complete:', file)



# os.system('pause')