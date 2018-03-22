import Variables as vb
import Previsualizar as pr
import wx
from functools import partial


def cargar_archivo(e, numero, texto):
    cargar = wx.Frame(None, -1, 'win.py')
    cargar.SetSize(0, 0, 200, 50)

    dlg = wx.FileDialog(cargar, texto)

    if dlg.ShowModal() == wx.ID_OK:
        # return dlg.GetPath()
        if numero == 1:
            vb.video = dlg.GetPath()
            print(vb.video)
            cuadro1.write(dlg.GetPath())
        else:
            vb.csv = dlg.GetPath()
            cuadro2.write(dlg.GetPath())


app = wx.App()
menu_principal = wx.Frame(None)
menu_principal.Bind(wx.EVT_CLOSE, vb.cerrar)

panel_principal = wx.Panel(menu_principal)

texto1 = wx.StaticText(panel_principal, label="Video", pos=(20, 40))
texto2 = wx.StaticText(panel_principal, label="CSV", pos=(20, 80))

cuadro1 = wx.TextCtrl(panel_principal, value=vb.video, pos=(70, 38), size=(175, -1))
cuadro2 = wx.TextCtrl(panel_principal, value=vb.csv, pos=(70, 78), size=(175, -1))

boton1 = wx.Button(panel_principal, label="Cargar video", pos=(260, 37))
boton2 = wx.Button(panel_principal, label="Cargar CSV", pos=(260, 77))
boton_salir=wx.Button(panel_principal,label="Salir",pos=(20,120))
boton_previsualizar = wx.Button(panel_principal, label="Previsualizar video", pos=(120, 120))
boton_gen = wx.Button(panel_principal, label="Generar video", pos=(250, 120))

boton1.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el video", numero=1))
boton2.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el CSV", numero=2))
boton_salir.Bind(wx.EVT_BUTTON,vb.cerrar)
boton_previsualizar.Bind(wx.EVT_BUTTON,pr.previsualizar)


menu_principal.Show()
app.MainLoop()