import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk

from gtk3.signal_handlers import SignalHandlers
from utils.oauth2 import ApiAccess


MENU_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="app-menu">
    <section>
      <attribute name="label" translatable="yes">Change label</attribute>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">String 1</attribute>
        <attribute name="label" translatable="yes">String 1</attribute>
      </item>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">String 2</attribute>
        <attribute name="label" translatable="yes">String 2</attribute>
      </item>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">String 3</attribute>
        <attribute name="label" translatable="yes">String 3</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="action">win.maximize</attribute>
        <attribute name="label" translatable="yes">Maximize</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="action">app.about</attribute>
        <attribute name="label" translatable="yes">_About</attribute>
      </item>
      <item>
        <attribute name="action">app.quit</attribute>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="accel">&lt;Primary&gt;q</attribute>
    </item>
    </section>
  </menu>
</interface>
"""


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="org.komunitin.komunitinLite",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs
        )
        self.window = None
        self.access = None

    def do_startup(self):
        Gtk.Application.do_startup(self)
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about)
        self.add_action(action)
        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)
        builder = Gtk.Builder.new_from_string(MENU_XML, -1)
        self.set_app_menu(builder.get_object("app-menu"))
#        self.access = ApiAccess()

    def do_activate(self):
        if not self.window:
            builder = Gtk.Builder()
            builder.add_from_file("./gtk3/glade/application_window.glade")
            self.window = builder.get_object("main_window")
            builder.connect_signals(SignalHandlers())
            self.add_window(self.window)
        self.window.show_all()

    def on_about(self, action, param):
        pass
        #about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        #about_dialog.present()

    def on_quit(self, action, param):
        self.quit()
