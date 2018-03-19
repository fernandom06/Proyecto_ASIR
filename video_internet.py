# import wx python
# Ejemplo que al darle al play reproduce lo que haya en mp3_path, mp3 y wav, de video con mp4 comprobado


import wx, wx.media


# ----------------------------------------------------------------------
def button_pressed(e):
    """this function gets called when btn gets clicked,
    which loads the mp3 file into the player"""
    print ('button pressed')
    frm.player.Load(mp3_path)


# ----------------------------------------------------------------------
def song_is_loaded(e):
    """this function gets called when the EVT_MEDIA_LOADED is created
    , then  it plays the song that gets loaded."""
    frm.player.Play()
    print ('evt loaded')


# sets the path to the mp3 file
mp3_path = r'madrid.mp4'

# creates a wxPython App with the 'print' output sent to the terminal, rather
# than the wx log
app = wx.App(redirect=False)

# create  Frame without any parent
frm = wx.Frame(None, id=wx.ID_ANY)
# creates the MediaCtrl, invisible to us, with the frame as a parent, and
# the WMP10 backend set
frm.player = wx.media.MediaCtrl(parent=frm, szBackend=wx.media.MEDIABACKEND_WMP10)

# Binds the EVT_MEDIA_LOADED to the function song_is_loaded written above,
# so that when the song gets loaded to memory, it actually gets played.
frm.Bind(wx.media.EVT_MEDIA_LOADED, song_is_loaded)

# a wx Sizer so that the two widjets gets places
main_sizer = wx.BoxSizer()

# the play button, to start the load
btn = wx.Button(frm, label='Play')
# binding the load mp3 function above to the clicking of this button
btn.Bind(wx.EVT_BUTTON, button_pressed)

# add the player and the button the sizer, to be placed on the screen
main_sizer.Add(frm.player)
main_sizer.Add(btn)

# declare the main_sizer as the top sizer for the entire frame
frm.SetSizer(main_sizer)
# show the frame to the user
frm.Show()

# start the mainloop, required for any wxPython app. It kicks off the logic.
print ('running')
app.MainLoop()