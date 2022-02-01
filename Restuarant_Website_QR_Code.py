# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:09:10 2022

@author: RahbarZ
"""
import qrcode
img = qrcode.make("https://www.jaflongcurry.co.uk/")
img.save("Restuarant.jpg")


