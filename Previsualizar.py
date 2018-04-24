from functools import partial
import wx
import wx.media
from PIL import Image
import Graficas as gr
import Variables as vb


def previsualizar(e):
    def cargado(e):
        # Lanza el video y si es la primera vez posiciona el video donde el usuario desea
        barra_mover.Show()
        if vb.c_segundos == 0:
            player.Seek(vb.s_entrada * 1000)
        player.Play()
        timer.Start(50)
        vb.c_segundos = 1

    def pause(e):
        # Para el video y el timer que mueve la barra
        player.Pause()
        timer.Stop()

    def grabar_video(e):
        # Esconde los controles no permite redimensionar la pantalla y
        # lanza el video desde el principio a los 5 segundos para grabar la pantalla
        reproductor.SetWindowStyleFlag(style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        reproductor.SetSize(reproductor.GetSize())
        panel_player.SetBackgroundColour(vb.back_rep)
        panel_grafica.SetBackgroundColour(vb.back_rep)
        reproductor.Refresh()
        player.Stop()
        boton_play.Hide()
        boton_pause.Hide()
        boton_atras.Hide()
        boton_grafica.Hide()
        boton_grabar.Hide()
        slider_player.Hide()
        timer_grabar.Start(5000, True)
        barra_mover.SetPosition((vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))
        vb.c_segundos = 0

    def pinchar(e, widget):
        if widget.HasCapture():
            widget.ReleaseMouse()
        widget.CaptureMouse()
        x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
        originx, originy = widget.GetPosition()
        dx = x - originx
        dy = y - originy
        vb.delta = (dx, dy)
        widget.Bind(wx.EVT_MOTION, partial(arrastrar, widget=widget))

    def arrastrar(e, widget):
        if e.Dragging():
            x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
            fp = (x - vb.delta[0], y - vb.delta[1])
            widget.Bind(wx.EVT_LEFT_UP, partial(soltar, widget=widget))
            widget.Move(fp)

    def soltar(e, widget):
        if widget.HasCapture():
            widget.ReleaseMouse()
        reproductor.Refresh()

    def actualizar(e):
        # Funcion que actualiza la posicion de la barra en la grafica dependiendo del momento del video
        barra_mover.Show()
        # Si slider valor maximo se para el video
        if slider_player.GetMax() == slider_player.GetValue():
            parar_video()
        # Establecer el valor del slider segun la posicion del video
        tiempo = vb.pixeles_grafica / (vb.s_salida - vb.s_entrada)
        slider_player.SetValue((player.Tell() / 1000))
        print(slider_player.GetValue())
        print(player.Tell())
        movimiento = wx.Point(vb.l_grafica + vb.l_barra + ((player.Tell()/1000 - vb.s_entrada) * tiempo),
                              vb.t_grafica + vb.t_barra)
        barra_mover.SetPosition(movimiento)

    def par_slider(e):
        # Cuando se quiere mover el slider se para el timer
        timer.Stop()

    def mov_slider(e):
        # Cuando se suelta para reubicar el slider hay que avanzar o retroceder el video y volver a lanzar el timer
        player.Seek(slider_player.GetValue() * 1000)
        timer.Start(50)

    def parar_video():
        # Cuando se llega al final del video se para el video y se para el timer
        player.Pause()
        timer.Stop()
        vb.c_segundos = 0

    def atras(e):
        # Funcion para volver al formulario principal
        timer.Stop()
        vb.c_segundos = 0
        vb.c_grafica = 0
        reproductor.Destroy()

    def regrafica(e):
        barra_mover.Hide()
        gr.grafica()
        grafica.SetBitmap(wx.Bitmap(name="grafico.png"))

    def resize(e):
        # Funcion para redimensionar la imagen ajustandolo al tamaño de la ventana
        imagen = Image.open("grafico.png")
        guardar = imagen.resize((int(vb.w_grafica), int(vb.h_grafica)))
        guardar.save("otra.png")
        grafica.SetBitmap(wx.Bitmap(name="otra.png"))
        imagen = Image.open("socio2.png")
        guardar = imagen.resize((int(vb.w_logo), int(vb.h_logo)))
        guardar.save("logo.png")
        logo.SetBitmap(wx.Bitmap(name="logo.png"))

    def responsive(e):
        # Funcion para redimensionar todos los elementos y ajustarlos al tamaño de la ventana
        barra_mover.Hide()
        # Obtener ancho y alto de la ventana
        w, h = reproductor.GetSize()

        # Calcular los pixeles solo de la grafica
        vb.pixeles_grafica = vb.pixeles_grafica * w / vb.w_ant

        # Cambios al player y a su Panel
        vb.w_player = vb.w_player * w / vb.w_ant
        vb.h_player = vb.h_player * h / vb.h_ant
        vb.w_panel_player = vb.w_panel_player * w / vb.w_ant
        vb.h_panel_player = vb.h_panel_player * h / vb.h_ant
        vb.l_panel_player = vb.l_panel_player * w / vb.w_ant
        vb.t_panel_player = vb.t_panel_player * h / vb.h_ant
        player.SetSize(vb.w_player, vb.h_player)
        panel_player.SetSize(vb.w_panel_player, vb.h_panel_player)
        panel_player.SetPosition(pt=(vb.l_panel_player, vb.t_panel_player))

        # Cambios al logo
        vb.w_logo = vb.w_logo * w / vb.w_ant
        vb.h_logo = vb.h_logo * h / vb.h_ant
        vb.l_logo = vb.l_logo * w / vb.w_ant
        vb.t_logo = vb.t_logo * h / vb.h_ant
        logo.SetSize(vb.w_logo, vb.h_logo)
        logo.SetPosition(pt=(vb.l_logo, vb.t_logo))

        # Camios Slider
        vb.w_slider = vb.w_slider * w / vb.w_ant
        vb.h_slider = vb.h_slider * h / vb.h_ant
        vb.t_slider = vb.t_slider * h / vb.h_ant
        slider_player.SetSize(vb.w_slider, vb.h_slider)
        slider_player.SetPosition(pt=(vb.l_player, vb.t_player + vb.t_slider))

        # Cambios Botones
        vb.w_play = vb.w_play * w / vb.w_ant
        vb.h_play = vb.h_play * h / vb.h_ant
        vb.t_play = vb.t_play * h / vb.h_ant
        boton_play.SetSize(vb.w_play, vb.h_play)
        boton_play.SetPosition(pt=(vb.l_player, vb.t_player + vb.t_play))

        vb.w_pause = vb.w_pause * w / vb.w_ant
        vb.h_pause = vb.h_pause * h / vb.h_ant
        vb.l_pause = vb.l_pause * w / vb.w_ant
        vb.t_pause = vb.t_pause * h / vb.h_ant
        boton_pause.SetSize(vb.w_pause, vb.h_pause)
        boton_pause.SetPosition(pt=(vb.l_player + vb.l_pause, vb.t_player + vb.t_pause))

        vb.w_atras = vb.w_atras * w / vb.w_ant
        vb.h_atras = vb.h_atras * h / vb.h_ant
        vb.l_atras = vb.l_atras * w / vb.w_ant
        vb.t_atras = vb.t_atras * h / vb.h_ant
        boton_atras.SetSize(vb.w_atras, vb.h_atras)
        boton_atras.SetPosition(pt=(vb.l_player + vb.l_atras, vb.t_player + vb.t_atras))

        vb.w_grabar = vb.w_grabar * w / vb.w_ant
        vb.h_grabar = vb.h_grabar * h / vb.h_ant
        vb.l_grabar = vb.l_grabar * w / vb.w_ant
        vb.t_grabar = vb.t_grabar * h / vb.h_ant
        boton_grabar.SetSize(vb.w_grabar, vb.h_grabar)
        boton_grabar.SetPosition(pt=(vb.l_player + vb.l_grabar, vb.t_player + vb.t_grabar))

        # Mover el boton de regrafica
        vb.w_regrafica = vb.w_regrafica * w / vb.w_ant
        vb.h_regrafica = vb.h_regrafica * h / vb.h_ant
        vb.l_regrafica = vb.l_regrafica * w / vb.w_ant
        vb.t_regrafica = vb.t_regrafica * h / vb.h_ant
        boton_grafica.SetSize(vb.w_regrafica, vb.h_regrafica)
        boton_grafica.SetPosition(pt=(vb.l_player + vb.l_regrafica, vb.t_player + vb.t_regrafica))

        # Grafica
        vb.w_grafica = vb.w_grafica * w / vb.w_ant
        vb.h_grafica = vb.h_grafica * h / vb.h_ant
        vb.w_panel_grafica = vb.w_panel_grafica * w / vb.w_ant
        vb.h_panel_grafica = vb.h_panel_grafica * h / vb.h_ant
        vb.l_panel_grafica = vb.l_panel_grafica * w / vb.w_ant
        vb.t_panel_grafica = vb.t_panel_grafica * h / vb.h_ant
        grafica.SetSize(vb.w_grafica, vb.h_grafica)
        panel_grafica.SetSize(vb.w_panel_grafica, vb.h_panel_grafica)
        panel_grafica.SetPosition(pt=(vb.l_panel_grafica, vb.t_panel_grafica))

        # Barra
        vb.w_barra = vb.w_barra * w / vb.w_ant
        vb.h_barra = vb.h_barra * h / vb.h_ant
        vb.l_barra = vb.l_barra * w / vb.w_ant
        vb.t_barra = vb.t_barra * h / vb.h_ant
        barra_mover.SetSize(vb.w_barra, vb.h_barra)
        barra_mover.SetPosition(pt=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))

        # Calcular pulgadas para la grafica
        vb.w_inch = vb.w_grafica / 100
        vb.h_inch = vb.h_grafica / 100

        # Guaradar los nuevos valores de ancho y alto de la ventana
        vb.w_ant = w
        vb.h_ant = h
        vb.w_ant_grafica = vb.w_grafica
        vb.h_ant_grafica = vb.h_grafica

    # LLamar a la funcion grafica para crear la grafica
    vb.barra_tiempo = gr.grafica()

    # Crear ventana para el video
    reproductor = wx.Frame(None, size=(1440, 900))
    reproductor.SetBackgroundColour(vb.back_rep)
    reproductor.Maximize()
    reproductor.Bind(wx.EVT_SIZE, responsive)
    reproductor.Bind(wx.EVT_CLOSE, atras)
    reproductor.Bind(wx.EVT_MOUSE_CAPTURE_CHANGED, resize)

    # main_sizer = wx.BoxSizer()
    panel_player = wx.Panel(reproductor, size=(640, 500), pos=(640, 0))
    panel_player.Layout()
    panel_player.SetBackgroundColour(wx.YELLOW)
    panel_player.Bind(wx.EVT_LEFT_DOWN, partial(pinchar, widget=panel_player))
    panel_grafica = wx.Panel(reproductor, size=(930, 580), pos=(445, 530))
    panel_grafica.Layout()
    panel_grafica.SetBackgroundColour(wx.YELLOW)
    panel_grafica.Bind(wx.EVT_LEFT_DOWN, partial(pinchar, widget=panel_grafica))

    # main_sizer.Add(panel_reproductor)

    # Video
    boton_play = wx.BitmapButton(panel_player, bitmap=wx.Bitmap("player_play.png"),
                                 pos=(vb.l_player, vb.t_player + vb.t_play), size=(vb.w_play, vb.h_play))
    boton_play.Bind(wx.EVT_BUTTON, cargado)
    boton_pause = wx.BitmapButton(panel_player, bitmap=wx.Bitmap("player_pause.png"),
                                  pos=(vb.l_player + vb.l_pause, vb.t_player + vb.t_pause),
                                  size=(vb.w_pause, vb.h_pause))
    boton_pause.Bind(wx.EVT_BUTTON, pause)
    boton_atras = wx.Button(panel_player, label="Atrás", pos=(vb.l_player + vb.l_atras, vb.t_player + vb.t_atras),
                            size=(vb.w_grabar, vb.h_grabar))
    boton_atras.Bind(wx.EVT_BUTTON, atras)
    boton_grabar = wx.Button(panel_player, label="Grabar Video",
                             pos=(vb.l_player + vb.l_grabar, vb.t_player + vb.t_grabar),
                             size=(vb.w_grabar, vb.h_grabar))
    boton_grabar.Bind(wx.EVT_BUTTON, grabar_video)
    boton_grafica = wx.Button(panel_player, label="Recalcular Grafica",
                              pos=(vb.l_player + vb.l_regrafica, vb.t_player + vb.t_regrafica),
                              size=(vb.w_regrafica, vb.h_regrafica))
    boton_grafica.Bind(wx.EVT_BUTTON, regrafica)

    player = wx.media.MediaCtrl(panel_player, pos=(vb.l_player, vb.t_player), size=(vb.w_player, vb.h_player))
    player.Load(vb.video)

    # Slider que llevara el tiempo del video
    slider_player = wx.Slider(panel_player, pos=(vb.l_player, vb.t_player + vb.t_slider),
                              size=(vb.w_slider, vb.h_slider))
    if vb.s_salida != 0:
        slider_player.SetRange(vb.s_entrada, vb.s_salida)
    else:
        slider_player.SetRange(vb.s_entrada, len(vb.barra_tiempo))

    slider_player.Bind(wx.EVT_SCROLL_THUMBTRACK, par_slider)
    slider_player.Bind(wx.EVT_SCROLL_THUMBRELEASE, mov_slider)

    # Grafica

    grafica = wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="grafico.png"), pos=(vb.l_grafica, vb.t_grafica),
                              size=(vb.w_grafica, vb.h_grafica))

    logo = wx.StaticBitmap(reproductor, -1, wx.Bitmap(name="socio2.png"), pos=(vb.l_logo, vb.t_logo),
                           size=(vb.w_logo, vb.h_logo))
    logo.Bind(wx.EVT_LEFT_DOWN, partial(pinchar, widget=logo))

    # Timer que se lanza cada 250 ms para actualizar la barra que se mueve por el gráfico
    timer = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, actualizar, timer)

    # Timer que al dar al boton de grabar tendra que lanzar el video para grabar
    timer_grabar = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, cargado, timer_grabar)

    # Introducir la barra encima del gráfico
    barra_mover = wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="barra2.png"),
                                  pos=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra),
                                  size=(vb.w_barra, vb.h_barra))
    barra_mover.Hide()

    # Sizers

    # reproductor.SetSizer(main_sizer)
    # reproductor.Layout()

    reproductor.Show()
    reproductor.Centre(wx.BOTH)
