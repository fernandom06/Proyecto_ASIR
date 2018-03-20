import wx


def foo(e,texto):
    adios="adios"
    print("adios")
    return {
        "adios":adios
    }


app=wx.App()
hola="hola"

frame=wx.Frame(None)

btn=wx.Button(frame,label="Prueba")
btn.Bind(wx.EVT_BUTTON,lambda e,texto=hola:foo(e,texto))

frame.Show()
app.MainLoop()