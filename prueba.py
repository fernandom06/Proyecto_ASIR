import interfaz
import wx

menu=interfaz.Menu()

panel=interfaz.Panel(menu,0,0,400,300)
texto1=interfaz.Texto(panel,"Video",20,40)
texto2=interfaz.Texto(panel,"CSV",20,80)

cuadro1=interfaz.CuadroTexto(panel,"Introduce el video",70,38,175,-1)
cuadro2=interfaz.CuadroTexto(panel,"Introduce el CSV",70,78,175,-1)

btn_vid=interfaz.Boton(panel,"Cargar video",250,37)
btn_csv=interfaz.Boton(panel,"Cargar CSV",250,77)

btn_csv.Bind(wx.EVT_BUTTON, btn_csv.cargar_archivo,btn_csv)
#hola=btn_csv.cargar_archivo()
#print(hola)

menu.Show()
menu.main_loop()
