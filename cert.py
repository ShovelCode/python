#!/usr/bin/python
'''
Create an HTML certificate
'''

from __future__ import print_function #version 2 compatibility
import time, sys, webbrowser

if sys.version_info[0] == 2:
    input = raw_input
    import cgi
    htmlescape = cgi.escape
    #begin on page 1463
