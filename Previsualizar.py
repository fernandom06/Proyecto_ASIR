import wx
import wx.media
import Graficas as gr
import Variables as vb


def previsualizar(e):
    def cargado(e):
        if vb.c_segundos == 1:
            player.Seek(vb.s_entrada * 1000)
        player.Play()
        timer.Start(250)
        vb.c_segundos = 0

    def pause(e):
        player.Pause()
        timer.Stop()

    def actualizar(e):
        # Si slider valor maximo se para el video
        if slider_player.GetMax() == slider_player.GetValue():
            parar_video()
        # Establecer el valor del slider segun la posicion del video
        tiempo = 504 / (vb.s_salida - vb.s_entrada)
        slider_player.SetValue((player.Tell() / 1000))
        movimiento = wx.Point(vb.l_gr + 116 + ((slider_player.GetValue() - vb.s_entrada) * tiempo), vb.t_gr + 30)
        barra_mover.SetPosition(movimiento)

    def par_slider(e):
        timer.Stop()

    def mov_slider(e):
        player.Seek(slider_player.GetValue() * 1000)
        timer.Start(250)

    def parar_video():
        player.Pause()
        timer.Stop()
        vb.c_segundos = 1

    def atras(e):
        pause
        vb.c_segundos = 1
        reproductor.Destroy()

    vb.barra_tiempo = gr.grafica()

    # Crear ventana para el video
    reproductor = wx.Frame(None, size=(1500, 1000))
    reproductor.SetBackgroundColour(vb.back_rep)
    reproductor.Maximize()
    reproductor.Bind(wx.EVT_CLOSE, atras)

    main_sizer = wx.BoxSizer()
    panel_reproductor = wx.Panel(reproductor)
    main_sizer.Add(panel_reproductor)

    # Video
    boton_play = wx.BitmapButton(panel_reproductor, bitmap=wx.Bitmap("player_play.png"), pos=(vb.l_rep, vb.t_rep + 450))
    boton_pause = wx.BitmapButton(panel_reproductor, bitmap=wx.Bitmap("player_pause.png"),
                                  pos=(vb.l_rep + 45, vb.t_rep + 450))
    boton_atras = wx.Button(panel_reproductor, label="Atrás", pos=(vb.l_rep + 90, vb.t_rep + 464))
    boton_play.Bind(wx.EVT_BUTTON, cargado)
    boton_pause.Bind(wx.EVT_BUTTON, pause)
    boton_atras.Bind(wx.EVT_BUTTON, atras)

    player = wx.media.MediaCtrl(panel_reproductor, pos=(vb.l_rep, vb.t_rep), size=(640, 400))
    # player.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_VOLUME)
    player.Load(vb.video)

    # Slider que llevara el tiempo del video
    slider_player = wx.Slider(panel_reproductor, pos=(vb.l_rep, vb.t_rep + 420), size=(640, -1))
    if vb.s_salida != 0:
        slider_player.SetRange(vb.s_entrada, vb.s_salida)
    else:
        slider_player.SetRange(vb.s_entrada, len(vb.barra_tiempo))

    slider_player.Bind(wx.EVT_SCROLL_THUMBTRACK, par_slider)
    slider_player.Bind(wx.EVT_SCROLL_THUMBRELEASE, mov_slider)

    # Grafica

    wx.StaticBitmap(panel_reproductor, -1, wx.Bitmap(name="grafico.png"), pos=(vb.l_gr, vb.t_gr), size=(640, 480))
    wx.StaticBitmap(panel_reproductor, -1, wx.Bitmap(name="socio2.png"), pos=(vb.l_soc, vb.t_soc), size=(431, 183))

    # Timer que se lanza cada 250 ms para actualizar la barra que se mueve por el gráfico
    timer = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, actualizar, timer)
    # Introducir la barra encima del gráfico
    barra_mover = wx.StaticBitmap(panel_reproductor, -1, wx.Bitmap(name="barra2.png"), pos=(vb.l_gr + 116, vb.t_gr + 30))

    # Sizers

    reproductor.SetSizer(main_sizer)
    reproductor.Layout()

    reproductor.Show()
    reproductor.Centre(wx.BOTH)
