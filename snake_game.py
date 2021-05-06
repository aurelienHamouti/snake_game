# -*- coding: utf-8 -*-
import ressources.welcome as welcomePage
try:
    welcomePage.start() #Start welcome page
except ValueError:
    print("An exception occurred : " + ValueError)