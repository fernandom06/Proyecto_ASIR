import wx
import Variables as vb
class Klass:
    o="hola"

def onclick(e,numero1,numero2):
    numero1=numero1
    numero2=numero2
    vb.video=numero1+numero2
    print(vb.video)




app = wx.App()
frame = wx.Frame(None)
objeto=Klass
print(objeto.o)


panel = wx.Panel(frame)

boton = wx.Button(panel)
boton.Bind(wx.EVT_BUTTON,lambda e,numero1=34,numero2=56:onclick(e,numero1,numero2))
print(vb.video)



frame.Show()
app.MainLoop()



