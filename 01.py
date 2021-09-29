import tkinter
from tkinter import filedialog
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
    time = str(datetime.datetime.today())
    qr_rename = str('QRCode ' + time[0:4] +'_'+ time[5:7]+'_'+ time[8:10]+'_'+ time[11:13] +'_'+time[14:16]+'_'+time[17:19]+'_'+time[20:26]+'.png')
    get_txt = txt.get()
    qr_image = qrcode.make(get_txt)
    qr_image_resize = qr_image.resize((300,300))
    pre_img = ImageTk.PhotoImage(qr_image_resize)
    img_preview = tkinter.Label(image=pre_img,bd=0)
    img_preview.image = pre_img
    img_preview.place(x=150,y=140)
    

# making a window
qr_code = tkinter.Tk()
qr_code.title('QR Code')
qr_code.geometry('600x500')
qr_code.resizable(0,0)
qr_code.configure(bg='LightSkyBlue1')


# text imput
txt = tkinter.Entry(qr_code,bd=0,font=('Arila', 15),width=50)
txt.place(x=30,y=30)
# making creat button
but_creat = tkinter.Button(qr_code,text='Creat',font=('Arial',15),bd=0,bg='LightPink1',fg='DarkBlue', activebackground='white',activeforeground='DarkBlue',command=qr_preview)
but_creat.place(x=70,y=90)

# making save button
btn_save = tkinter.Button(qr_code,text='Save',font=('Arial',16),bd=0,bg='LightPink1',fg='DarkBlue', activebackground='white',activeforeground='DarkBlue',command=qr_save)
btn_save.place(x=470,y=90)
qr_code.mainloop()
