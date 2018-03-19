import wx.media

def cargado(e):
    print("cargado")
    frame.player.Play()

app=wx.App()
frame=wx.Frame(None)

frame.player=wx.media.MediaCtrl(parent=frame,szBackend=wx.media.MEDIABACKEND_WMP10)
frame.player.Load(r"Cabecera.mp4")
frame.player.Bind(wx.media.EVT_MEDIA_LOADED,cargado)


frame.Show()
app.MainLoop()

