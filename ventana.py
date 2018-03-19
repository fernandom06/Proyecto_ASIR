import wx
import wx.lib.buttons as buttons
import sys


def cargar_archivo(e):
    # Funcion que se encarga de cargar la ruta de un archivo del SO
    cargar = wx.Frame(None, -1, 'win.py')
    cargar.SetSize(0, 0, 200, 50)

    dlg = wx.FileDialog(cargar, "elige el archivo")

    if dlg.ShowModal() == wx.ID_OK:
        print(dlg.GetPath())
        return dlg.GetPath()



def cerrar(e):
    # Funcion para cerrar el programa
    sys.exit(0)


app = wx.App()

# Ventana principal
frame = wx.Frame(None, -1, 'Ventana', size=(400, 300))

panel = wx.Panel(frame)

wx.StaticText(panel, label="Video", pos=(20, 40))
basicText = wx.TextCtrl(panel, 1, "Introduce el video", pos=(70, 38), size=(175, -1))
basicText.SetInsertionPoint(0)

wx.StaticText(panel, label="CSV", pos=(20, 80))
basicText = wx.TextCtrl(panel, 1, "Introduce el CSV", pos=(70, 78), size=(175, -1))
basicText.SetInsertionPoint(0)

# Boton Video
btn_vid = buttons.GenButton(panel, label="Cargar Video", pos=(250, 37))
btn_vid.Bind(wx.EVT_BUTTON, cargar_archivo,btn_vid)

# Boton CSV
btn_csv = buttons.GenButton(panel, label="Cargar CSV", pos=(250, 77))
btn_csv.Bind(wx.EVT_BUTTON, cargar_archivo,btn_csv)

# Boton Salir
btn_salir = buttons.GenButton(panel, label="Salir", pos=(30, 120))
btn_salir.Bind(wx.EVT_BUTTON, cerrar)

frame.Bind(wx.EVT_CLOSE, cerrar)
frame.Show()

app.MainLoop()

"""
class MyForm(wx.Frame):


    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Button Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)

        button = wx.Button(panel, id=wx.ID_ANY, label="Press Me")
        button.Bind(wx.EVT_BUTTON, self.onButton)
        # self.Bind(wx.EVT_BUTTON, self.onButton, button)


    # ----------------------------------------------------------------------
    def onButton(self, event):
        # This method is fired when its corresponding button is pressed
        print("Button pressed!")


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
"""
"""
# Cerrar el Programa
salir = buttons.GenButton(panel, -1, "Salir", pos=(50, 100))
salir.Bind(wx.EVT_BUTTON, cerrar)
elegir_csv = wx.Button(panel, label="elegir_csv", pos=(20, 200))
elegir_csv.Bind(wx.EVT_BUTTON, cargar_archivo)
# Evento para cuando se cierra la ventana principal
# salir=wx.Button(panel,label="Salir",pos=(120,200))
# salir.Bind(wx.EVT_BUTTON,n_handle,salir)
frame.Bind(wx.EVT_CLOSE,cerrar)
"""
"""
Aplicacion que abre una ventana del explorador para elegir un archivo

app=wx.App()

frame = wx.Frame(None, -1, 'win.py')
frame.SetSize(0, 0, 200, 50)

dlg=wx.FileDialog(frame,"elige el archivo")

dlg.ShowModal()

"""
"""
Aplicacion que muestra un cuadro de dialogo y muestra por pantalla lo que introduces si le das a OK

app = wx.App()

frame = wx.Frame(None, -1, 'win.py')
frame.SetSize(0, 0, 200, 50)

# Create text input
dlg = wx.TextEntryDialog(frame, 'Enter some text', 'Text Entry')
dlg.SetValue("Default")
if dlg.ShowModal() == wx.ID_OK:
    print('You entered: %s\n' % dlg.GetValue())
dlg.Destroy()
"""
"""
Mostrar boton en una ventana(sin terminar)
def hola():
    print("hola")

app = wx.App()
frame = wx.Frame(None, title="principal",name="prin")
#ventana=wx.Frame(frame)
salir=wx.Button(frame,id=2,label="salir",pos=(225, 5), size=(1, 2))


frame.Show()

app.MainLoop()
"""
"""
Muestra una interfaz de usuario, una ventana con una barra de herramientas

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fitem = fileMenu.Append(wx.ID_EXIT, 'salir', 'Fuera')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
"""
