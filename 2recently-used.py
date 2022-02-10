#!/usr/bin/python3
#
# Add files to recently used GTK bookmarks
#   ~/.local/share/recently-used.xbel
#
# Copyright (C) 2022 Melon (https://github.com/Mhlov)
#
# LICENSE
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


def help():
    print("""2recently-used.py - Add files to recently used GTK bookmarks

    Usage:    2recently-used.py [files]
    """)

def make_uri(file):
    abs = os.path.abspath(file)
    uri = "file://" + abs
    return uri

def add_item(uri):
    rm = Gtk.RecentManager.get_default()
    rm.add_item(uri)

def commit():
    GLib.idle_add(Gtk.main_quit)
    Gtk.main()


def main():
    if len(sys.argv) > 1:
        for i in range(1,  len(sys.argv)):
            uri = make_uri(sys.argv[i])
            add_item(uri)
        commit()

    else:
        help()

    return 0

if __name__ == "__main__":
    sys.exit(main())

