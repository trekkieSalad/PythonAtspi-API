import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

'''
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
'''

# crear una ventana con una etiqueta y un boton
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        self.label = Gtk.Label("Hello World")
        self.box.pack_start(self.label, True, True, 0)
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)
        #add a spin button
        self.spin = Gtk.SpinButton()
        self.spin.set_range(0, 100)
        self.spin.set_increments(1, 1)
        self.spin.set_digits(0)
        self.box.pack_start(self.spin, True, True, 0)
        #add a fixed
        self.fixed = Gtk.Fixed()
        self.box.pack_start(self.fixed, True, True, 0)
        #add a table with random info
        self.table = Gtk.Table(2, 2, True)
        self.fixed.put(self.table, 10, 10)

        #add a accel group
        self.accel_group = Gtk.AccelGroup()
        self.add_accel_group(self.accel_group)
        #add a action bar
        self.action_bar = Gtk.ActionBar()
        self.box.pack_start(self.action_bar, True, True, 0)

        #add a appChooserButton
        #self.appChooserButton = Gtk.AppChooserButton.new(Gtk.DestDefaults.ALL)
        #self.action_bar.pack_start(self.appChooserButton)


        
    def on_button_clicked(self, widget):
        self.label.set_text("Goodbye World")

# iniciar la aplicacion
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()