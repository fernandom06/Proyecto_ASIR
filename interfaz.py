import wx
import wx.lib.buttons as buttons
import sys


class Menu(wx.Frame):
    # app=wx.App()
    def __init__(self, size=wx.DefaultSize):
        super().__init__(None, title="VentanaPrincipal", size=size)
    # def main_loop(self):
    #   self.app.MainLoop()


class Panel(wx.Panel):
    def __init__(self, parent, position=wx.DefaultPosition,size=wx.DefaultSize):
        super().__init__(parent=parent, size=size, pos=position)


class Boton(buttons.GenButton):
    def __init__(self, panel, label, left, top):
        super().__init__(parent=panel, label=label, pos=(left, top))

    def cargar_archivo(self, event):
        # Funcion que se encarga de cargar la ruta de un archivo del SO
        cargar = wx.Frame(None, -1, 'win.py')
        cargar.SetSize(0, 0, 200, 50)

        dlg = wx.FileDialog(cargar, "elige el archivo")

        if dlg.ShowModal() == wx.ID_OK:
            print(dlg.GetPath())

            return dlg.GetPath()


class Texto(wx.StaticText):
    def __init__(self, panel, label, left, top):
        super().__init__(parent=panel, label=label, pos=(left, top))


class CuadroTexto(wx.TextCtrl):
    def __init__(self, panel, value, position=wx.DefaultPosition, size=wx.DefaultSize):
        super().__init__(parent=panel, value=value, size=size, pos=position)
