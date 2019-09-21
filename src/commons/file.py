from werkzeug.utils import secure_filename
import os
from  src.models.file import File
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','bmp'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def save_file_in_local(file,filename):
   try:
       file.save(os.path.join('C:/Users/phongthien/Documents/Python Scripts',filename))
       link = File(name=filename,link='C:/Users/phongthien/Documents/Python Scripts/'+filename);
       link.save()
       return True,'C:/Users/phongthien/Documents/Python Scripts/'+filename
   except :

       return False