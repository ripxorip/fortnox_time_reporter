import sys
import gi
import time
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
        self.counter = 0
        self.timerActive = False

    def on_activate(self, app):
        # Create a Builder
        builder = Gtk.Builder()
        builder.add_from_file("fortnox_time_reporter-window.ui")

        # Obtain the button widget and connect it to a function
        startTimerButton = builder.get_object("startTimerButton")
        startTimerButton.connect("clicked", self.startTimerButtonClicked)

        finishReportButton = builder.get_object("finishReportButton")
        finishReportButton.connect("clicked", self.finishReportButtonClicked)

        reportButton = builder.get_object("reportButton")
        reportButton.connect("clicked", self.reportButtonClicked)

        resetButton = builder.get_object("resetButton")
        resetButton.connect("clicked", self.resetButtonClicked)

        self.timeLabel = builder.get_object("timeLabel")
        self.timeLabel.set_text("00:00:00")

        # Obtain and show the main window
        self.win = builder.get_object("FortnoxTimeReporterWindow")
        self.win.set_application(self)  # Application will close once it no longer has active windows attached to it
        self.win.present()

    def stopTimer(self):
        self.timerActive = False
        GLib.source_remove(self.timer_id)
        self.timeLabel.set_text("00:00:00")

    def startTimerButtonClicked(self, button):
        if not self.timerActive:
            self.counter = 0
            self.timerActive = True
            self.timer_id = GLib.timeout_add_seconds(1, self.updateCounter)

    def updateCounter(self):
        self.counter += 1
        self.timeLabel.set_text(time.strftime("%H:%M:%S", time.gmtime(self.counter)))  # Update the time label
        return True

    def finishReportButtonClicked(self, button):
        reportTime = self.counter
        self.stopTimer()
        # Ask the user if they want to report the time
        dialog = Gtk.MessageDialog(
            parent=self.win,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Do you want to report " + time.strftime("%H:%M:%S", time.gmtime(reportTime)) + "?"
        )
        dialog.set_title("Report time")
        response = dialog.set_visible(True)
        dialog.destroy()


    def reportButtonClicked(self, button):
        pass

    def resetButtonClicked(self, button):
        self.stopTimer()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
