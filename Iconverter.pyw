import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 3
__filename__ = "Iconverter"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("https://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("https://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("https://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("https://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

import shutil
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import *
from PIL import Image

constant_filename = ""
path_tmp = (os.path.join(os.environ['APPDATA'], "Icontemp"))
combobox_list = ("<Taille>", "16x16", "32x32", "64x64", "128x128", "256x256")
combobox_size = None

def selectsize(event):
    global combobox_size
    combobox_size = combobox_var.get().split("x")[0]
    if combobox_size == "<Taille>":
        showinfo(__filename__, "La taille est incorrecte, la convertion sera effectuée en 256x256 par défaut.")
        combobox_size = 256
    combobox_size = int(combobox_size)

def load_file():
    global fname_open
    fname_open = askopenfilename(filetypes=(("PNG", "*.png"),
                                        ("JPEG", "*.jpg *.jpeg *.jpe *.jfif"),
                                        ("GIF", "*.gif"),
                                        ("BMP", "*.bmp"),
                                        ("TIFF", "*.tif *.tiff"),
                                        ("TGA", "*.tga"),
                                        ("All", "*.png .jpg *.jpeg *.jpe *.jfif *.gif *.bmp *.tif *.tiff *.tga")))
    if fname_open:
        fbasename = os.path.basename(fname_open)
        try:
            constant_filename.set(str(fbasename))
        except:
            showerror(__filename__, "Le fichier " + fbasename + " n'a pas pu être lu !\n" + fname_open)

def convert_file():
    global fname_open
    global combobox_size
    try:
        fname_open
    except NameError:
        showerror(__filename__, "Aucun fichier n'a été choisi !")
    else:
        fname_save = asksaveasfile(mode='w', defaultextension=".ico", filetypes=[("Fichiers icones","*.ico")])
        if fname_save is None:
            return
        f_name = fname_save.name

        try:
            shutil.rmtree(path_tmp)
        except:
            pass

        os.mkdir(path_tmp)

        if combobox_size is not None:
            showinfo(__filename__, "Aucune taille n'a été donnée, la convertion sera effectuée en 256x256")
            combobox_size = 256

        img = Image.open(fname_open)
        img = img.resize((combobox_size, combobox_size), Image.ANTIALIAS)
        img.save(path_tmp + "\\resized.png", format="png", sizes=[(combobox_size, combobox_size)])

        img = Image.open(path_tmp + "\\resized.png")
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(path_tmp + "\\transparent.png", "PNG")

        img = Image.open(path_tmp + "\\transparent.png")
        img.save(f_name, format="ico", sizes=[(combobox_size, combobox_size)])

        shutil.rmtree(path_tmp)
        showinfo(__filename__, "Icone '" + os.path.basename(f_name) + "' à été crée avec succès !")
        iconverter.destroy()
        os._exit(0)

iconverter = Tk()
width = 600
height = 400
iconverter.update_idletasks()
x = (iconverter.winfo_screenwidth() - width) // 2
y = (iconverter.winfo_screenheight() - height) // 2
iconverter.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
iconverter.resizable(width=False, height=False)
iconverter.title(__filename__)
if os.path.exists(__iconpath__):
    iconverter.iconbitmap(__iconpath__)
iconverter.configure(background="#CCCCCC")
iconverter.configure(highlightbackground="#d9d9d9")
iconverter.configure(highlightcolor="black")
font1 = "-family {Rockwell Extra Bold} -size 14 -weight bold -slant roman -underline 0 -overstrike 0"
font2 = "-family {Rockwell Extra Bold} -size 16 -weight bold -slant roman -underline 0 -overstrike 0"

Label1 = Label(iconverter)
Label1.place(relx=0.1, rely=0.4, height=30, width=160)
Label1.configure(activebackground="#f9f9f9")
Label1.configure(activeforeground="black")
Label1.configure(background="#CCCCCC")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font=font1)
Label1.configure(foreground="#000000")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(text="Fichier :")

Text1 = Entry(iconverter)
Text1.place(relx=0.35, rely=0.4, relheight=0.08, relwidth=0.5)
Text1.configure(background="white")
Text1.configure(font=font1)
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(state="readonly")
Text1.configure(width=300)
constant_filename = StringVar()
Text1.configure(textvariable=constant_filename)

Button1 = Button(iconverter)
Button1.place(relx=0.39, rely=0.13, height=50, width=125)
Button1.configure(activebackground="#d9d9d9")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#CCCCCC")
Button1.configure(cursor="X_cursor")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font=font2)
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text="Ouvrir")
Button1.configure(command=load_file)

Button2 = Button(iconverter)
Button2.place(relx=0.386, rely=0.75, height=50, width=135)
Button2.configure(activebackground="#d9d9d9")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#CCCCCC")
Button2.configure(cursor="X_cursor")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font=font2)
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text="Convertir")
Button2.configure(command=convert_file)

combobox_var = StringVar()
combobox_var.set(combobox_list[0])

Combobox1 = Combobox(iconverter, textvariable=combobox_var, values=combobox_list, state="readonly", background="white")
Combobox1.place(relx=0.405, rely=0.58, relheight=0.08, relwidth=0.19)
Combobox1.configure(width=100)
Combobox1.configure(takefocus="")
Combobox1.configure(font=font1)
Combobox1.bind("<<ComboboxSelected>>", selectsize)

iconverter.mainloop()
