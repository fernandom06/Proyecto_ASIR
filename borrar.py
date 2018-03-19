import wx
import w

def cargado(e):
    player.Play()

app = wx.App()

frame = wx.Frame(None, title="Prueba", size=(1000, 800))

# Creacion de sizers
main_sizer = wx.GridSizer(2, 1, 0, 0)

sizer_video = wx.GridSizer(0, 2, 0, 0)
main_sizer.Add(sizer_video, 1, wx.EXPAND, 5)

sizer_grafica = wx.GridSizer(0, 2, 0, 0)
main_sizer.Add(sizer_grafica, 1, wx.EXPAND, 5)

panel_video = wx.Panel(frame)
sizer_video.Add(panel_video)

panel_grafica = wx.Panel(frame)
sizer_grafica.Add(panel_grafica)

# Video

player=wx.media.MediaCtrl(panel_video,pos=(250,0),size=(500,250))
player.Load("madrid.mp4")
panel_video.Bind(wx.media.EVT_MEDIA_LOADED, cargado)


# Graficas



# (Al final) Asignar el sizer orincipal a la ventana principal
frame.SetSizer(main_sizer)
frame.Layout()

frame.Centre(wx.BOTH)

frame.Show()
app.MainLoop()
