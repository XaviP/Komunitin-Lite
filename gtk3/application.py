
import gi
gi.require_version('Gtk', '3.0')  # noqa: E402
from gi.repository import Gio
from gi.repository import Gtk

from gtk3.window import AppWindow
from gtk3.menu import MENU_XML
from core.oauth2 import ApiAccess


class Application(Gtk.Application):
    def __init__(self, *args, config, **kwargs):
        super().__init__(
            *args,
            application_id="org.komunitin.komunitinLite",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs
        )
        self.config = config
        self.window = None
        self.access = None

    def do_startup(self):
        Gtk.Application.do_startup(self)
        action = Gio.SimpleAction.new("new_user", None)
        action.connect("activate", self.new_user)
        self.add_action(action)
        action = Gio.SimpleAction.new("make_transfer", None)
        action.connect("activate", self.make_transfer)
        self.add_action(action)
        action = Gio.SimpleAction.new("preferences", None)
        action.connect("activate", self.preferences)
        self.add_action(action)
        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)
        builder = Gtk.Builder.new_from_string(MENU_XML, -1)
        self.set_app_menu(builder.get_object("app-menu"))

        # Init access here, in do_activate seems a bad place.
        self.access = ApiAccess(self.config)
        self.access.get_local_auth()

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(
                application=self,
                title=_("Komunitin Lite"),
                access=self.access
            )
            self.add_window(self.window)
        self.window.show_all()
        if not self.access.has_access:
            self.window.show_dialog_login()
        else:
            self.window.show_dialog_loading()

    def new_user(self, action, param):
        self.window.show_dialog_login()

    def make_transfer(self, action, param):
        self.window.show_dialog_transfer()

    def preferences(self, action, param):
        self.window.show_dialog_preferences()

    def on_quit(self, action, param):
        self.quit()
