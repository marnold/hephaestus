
## File bitlespeak.py: BitleSpeak Main program 
## Matt Arnold <matt@thegnuguru.org> 6-30-10
##
## Copyright (c) 2010 Matt Arnold
## BitleSpeak is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## BitleSpeak is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with BitleSpeak.  If not, see <http://www.gnu.org/licenses/>.
 
import sys
import os.path
from bitle.unix.util import *
import gtk
from bitle.config import *



class BitleSpeak(object):
    
    def __init__(self, spk, xsel = False):
        
        ## see PyGtk Docs and data/ in source tree
        self.builder = gtk.Builder()
        ui_file_path = os.path.abspath(BASE_PATH 
                                       + '/data/Bitletoolbar.ui')
        if not os.path.isfile(ui_file_path):
        	ui_file_path = os.path.abspath(SITE_DATA_DIR + 
        					'/Bitletoolbar.ui')
        self.builder.add_from_file(ui_file_path)
        self.txtbuffers = [] ## Remember viewer goes in first
        dbg = self.builder.connect_signals(self)
        self.win = self.builder.get_object("mainWindow")
        tmp = self.builder.get_object("viewerBox")
        self.txtbuffers.append(tmp.get_buffer())
        tmp = self.builder.get_object("notesBox")
        self.txtbuffers.append(tmp.get_buffer())
        self.st_lbl = self.builder.get_object("statusLabel")
        self._icon()
        self.win.stick()
        self.win.show()
        if DEBUG:
            print "Unbound Events " + str(dbg)
        self.running = False  ## we don't want a seperate resume widget
        ## so this is used by play/stop widgets to determine behavior
        tspk, tcfg = spk ## tuple packing is apperently local scope only 
        self.xsel = xsel 
        self.lspkr = tspk
    
    def on_playButton_clicked(self, widget, data=None):
        """
        Speaks the clipboard contents when play is pressed
        """
        if self.xsel:
            tts = xsel_read()
        else:
            brd = gtk.clipboard_get()
            tts = str(brd.wait_for_text())
        self.running = True
        self.txtbuffers[0].set_text(tts)
        self.lspkr.speak(tts)
        self.running = False
        return
    
    def on_pauseButton_clicked(self, widget, data=None):
        

        btn = self.builder.get_object("pauseButton")
        print "tracing stack for pause"
        if self.running:
            self.lspkr.pause()
            btn.set_label('Resume')
        else:
            self.lspkr.resume()
            btn.set_label('Pause')
        return
    
    def on_stopButton_clicked(self, widget, data=None):
        
        if self.running:
            self.lspkr.stop()
            self.running = False
        else:
            return
    
    def on_aboutButton_clicked(self, widget):
        
        about = gtk.AboutDialog()
        about.set_program_name(APP_NAME)
        about.set_authors(APP_AUTHORS)
        about.set_version(APP_VER)
        about.set_copyright("(c) 2010 Matt Arnold")
        about.set_comments(APP_DESC)
        about.run()
        about.destroy()
    
    def on_prefButton_clicked(self, widget, data=None):
        
            md = gtk.MessageDialog(self.win, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, 
            gtk.BUTTONS_CLOSE, PREF_MSG)
            md.run()
            md.destroy()

    
    def on_mainWindow_destroy(self, widget, data=None):
        self.lspkr.stop()
        sys.exit(0)
    
    on_quitButton_clicked = on_mainWindow_destroy ## make gtk happy
    
    ## now a hack to get the icon in place
    def _icon(self):
    
    	chkpath = os.path.abspath(DATA_DIR + ICON_FILE_PATH)
    	if os.path.isfile(chkpath):
    		
    		self.win.set_icon_from_file(chkpath)
    		return
    	
    	chkpath = os.path.abspath(SITE_DATA_DIR + ICON_FILE_PATH)
    	if os.path.isfile(chkpath):
    		
    		self.win.set_icon_from_file(chkpath)
    		return
    	
    	chkpath = '/usr/share/pixmaps' + ICON_FILE_PATH
    	if os.path.isfile(chkpath):
    	
    		self.win.set_icon_from_file(chkpath)
    		return
    		
