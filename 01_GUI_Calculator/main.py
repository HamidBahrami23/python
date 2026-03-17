import gi
# We need to specify which version of GTK we want to use before importing it
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    """
    This class contains the functions (handlers) for the signals defined in Glade.
    The method names must match the handler names set in Glade's 'Signals' tab.
    """
    def onDestroy(self, *args):
        # This function is called when the user closes the window (clicks X)
        print("Application closed by user.")
        Gtk.main_quit()

    def on_button_clicked(self, button):
        # This matches the 'on_button_clicked' handler we set in Glade for the button
        print("Hello! The button was clicked.")
        # Example: Change the button label when clicked
        button.set_label("Clicked!")

# 1. Create a Builder object to load the UI file
builder = Gtk.Builder()

# 2. Load the description of the user interface from the .glade file
try:
    builder.add_from_file("gui.glade")
except Exception as e:
    print(f"Error loading UI file: {e}")
    exit(1)

# 3. Connect the signals defined in Glade to the python functions in the Handler class
builder.connect_signals(Handler())

# 4. Get the window object by its ID (which we set to 'main_window' in Glade)
window = builder.get_object("main_window")

# 5. Connect the window close event (clicking X) to quit the app properly
# Note: You should also add the 'onDestroy' handler to the "destroy" signal of the window in Glade,
# or connect it manually here like this:
window.connect("destroy", Gtk.main_quit)

# 6. Show the window and all its contents
window.show_all()

# 7. Start the GTK main event loop (waits for user actions)
print("Application started...")
Gtk.main()