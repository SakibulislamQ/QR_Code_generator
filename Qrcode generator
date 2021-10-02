import tkinter
from tkinter.filedialog import asksaveasfile
import qrcode
import datetime
from PIL import ImageTk
#2021-09-29 15:29:22.779873
# preview qr code
def qr_preview():
    get_txt = txt.get()
    qr_image = qrcode.make(get_txt)
    qr_image = qr_image.resize((300,300))
    pre_img = ImageTk.PhotoImage(qr_image)
    img_preview = tkinter.Label(image=pre_img,bd=0)
    img_preview.image = pre_img
    img_preview.place(x=150,y=140)
    
# saving qr _making
def qr_save():
    qr_preview()
    def rename():
        time = str(datetime.datetime.today())
        rename = time.replace('-','_')
        rename = rename.replace(':','_')
        return rename
    
    get_txt = txt.get()
    qr_make_image = qrcode.make(get_txt)

    file = asksaveasfile(title='Save image',filetypes = [('PNG','*.png'),('JPEG','*.jpg')],defaultextension = [('PNG','*.png'),('JPEG','*.jpg')],initialfile = rename())
    qr_make_image.save(file.name)
    
    
# making a window
qr_code = tkinter.Tk()
qr_code.title('QR Code Creator')
qr_code.iconbitmap('qrcodegen\qrcodecreator.ico')
qr_code.geometry('600x500')
qr_code.resizable(0,0)
qr_code.configure(bg='LightSkyBlue1')


# text imput
txt = tkinter.Entry(qr_code,bd=0,font=('Arila', 15),width=50)
txt.focus_set()
txt.place(x=30,y=30)
# making creat button
but_creat = tkinter.Button(qr_code,text='Create',font=('Arial',15),bd=0,bg='LightPink1',fg='DarkBlue', activebackground='white',activeforeground='DarkBlue',command=qr_preview)
but_creat.place(x=65,y=90)

# making save button
btn_save = tkinter.Button(qr_code,text='Save',font=('Arial',16),bd=0,bg='LightPink1',fg='DarkBlue', activebackground='white',activeforeground='DarkBlue',command=qr_save)
btn_save.place(x=470,y=90)
qr_code.mainloop()
