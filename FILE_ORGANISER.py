import os
import sys
import shutil
from glob import glob
import time
# from config import WIN_DOWNLOADS,LINUX_DOWNLOADS
from warnings import filterwarnings
filterwarnings('ignore')
WIN_DOWNLOADS   = r''
LINUX_DOWNLOADS = r''    


available_extensions = ['iso', 'zip', 'png', 'py', 'xlsx', 'gif', 'docx', 'csv', 'jpeg', 'gz', 
                        'svg', 'pdf', 'ipynb',  'jpg', 'exe', 'heic', 'deb']


def linuxCustomNotifier(header,message):
    pass


def windowsFileSorter(FILE_ARRAY):
    try:
        from win10toast import ToastNotifier # type: ignore
    except Exception as err:
        print('ToastNotifier NOT available for linux')
    iso_folder =r"{}\ISO".format(WIN_DOWNLOADS)
    exe_folder   = r"{}\EXE".format(WIN_DOWNLOADS)
    img_folder   = r"{}\Images".format(WIN_DOWNLOADS)
    video_folder = r"{}\Videos".format(WIN_DOWNLOADS)
    pdf_folder   = r"{}\PDF".format(WIN_DOWNLOADS)
    zip_folder   = r"{}\ZIP".format(WIN_DOWNLOADS)
    docx_folder  = r"{}\DOCX".format(WIN_DOWNLOADS)
    jupyter_folder = r"{}\JUPYTER_FILE".format(WIN_DOWNLOADS)
    csv_folder   = r"{}\CSV_EXCEL".format(WIN_DOWNLOADS)
    py_path      = r"{}\PY".format(WIN_DOWNLOADS)


    folder_extensions = { 
                    'iso':iso_folder, 
                    'zip':zip_folder, 
                    'png': img_folder, 
                    'py':py_path, 
                    'xlsx':csv_folder, 
                    'gif': img_folder, 
                    'docx': docx_folder, 
                    'csv':csv_folder, 
                    'jpeg': img_folder, 
                    'gz':zip_folder,     
                    'svg': img_folder, 
                    'pdf': pdf_folder, 
                    'ipynb':jupyter_folder,  
                    'jpg': img_folder, 
                    'exe': exe_folder, 
                    'heic': img_folder
                   }
    flag       = 0
    file_count = 0
    for FILE in FILE_ARRAY:
        if not os.path.isdir(FILE):
            if FILE.split('.')[-1] in available_extensions:
                destination_folder = folder_extensions[FILE.split('.')[-1]]
                shutil.move(FILE,destination_folder)
                print(destination_folder)
                flag = 1
                file_count+=1
    if flag:
        toaster = ToastNotifier()
        toaster.show_toast("FILE MOVEMENT",
                           f"FILES MOVED: {file_count} \n All Files Moved to respective Folder",
                            duration=5)
    elif(file_count<1):
        toaster = ToastNotifier()
        toaster.show_toast("FILE MOVEMENT",
                           "NO files to move")



def ubuntuFileSorter(FILE_ARRAY):
    iso_folder =r"{}/ISO".format(LINUX_DOWNLOADS)
    deb_folder   = r"{}/DEB".format(LINUX_DOWNLOADS)
    img_folder   = r"{}/Images".format(LINUX_DOWNLOADS)
    video_folder = r"{}/Videos".format(LINUX_DOWNLOADS)
    pdf_folder   = r"{}/PDF".format(LINUX_DOWNLOADS)
    zip_folder   = r"{}/ZIP".format(LINUX_DOWNLOADS)
    docx_folder  = r"{}/DOCX".format(LINUX_DOWNLOADS)
    jupyter_folder = r"{}/JUPYTER_FILE".format(LINUX_DOWNLOADS)
    csv_folder   = r"{}/CSV_EXCEL".format(LINUX_DOWNLOADS)
    py_path      = r"{}/PY".format(LINUX_DOWNLOADS)
    folder_extensions = { 
                    'iso':iso_folder, 
                    'zip':zip_folder, 
                    'png': img_folder, 
                    'py':py_path, 
                    'xlsx':csv_folder, 
                    'gif': img_folder, 
                    'docx': docx_folder, 
                    'csv':csv_folder, 
                    'jpeg': img_folder, 
                    'gz':zip_folder,     
                    'svg': img_folder, 
                    'pdf': pdf_folder, 
                    'ipynb':jupyter_folder,  
                    'jpg': img_folder, 
                    'deb': deb_folder, 
                    'heic': img_folder
                   }
    

    flag,file_count = 0,0
    for FILE in FILE_ARRAY:
        if not os.path.isdir(FILE):
            if FILE.split('.')[-1] in available_extensions:
                destination_folder = folder_extensions[FILE.split('.')[-1]]
                shutil.move(FILE,destination_folder)
                print(destination_folder)
                flag = 1
                file_count+=1
                




def main():
    if (sys.platform=='win32'): 
        win32_root_path = r'{}\*'.format(WIN_DOWNLOADS)
        x = glob(win32_root_path)
        windowsFileSorter(x)
    else:
        linux_root_path = r'{}/*'.format(LINUX_DOWNLOADS)
        listed_files = glob(linux_root_path)
        ubuntuFileSorter(listed_files)




if '__main__()':
    main()
