#!/usr/bin/python3
# -*- coding: utf-8 -*-


# To center window
# Without codinates

self.master.withdraw()
self.master.update_idletasks()  # Update "requested size" from geometry manager

x = (self.master.winfo_screenwidth() / 3 - self.master.winfo_reqwidth()) / 2
y = (self.master.winfo_screenheight() / 3 - self.master.winfo_reqheight()) / 2
self.master.geometry("+%d+%d" % (x, y))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position
self.master.deiconify()

# or with cordinates

self.master.resizable(False, False)
print(self.master.winfo_screenheight())
print(self.master.winfo_screenwidth())
#size_h=1050
#size_w=1680
self.window_height = 824
self.window_width = 1310

self.screen_width = self.master.winfo_screenwidth()
self.screen_height = self.master.winfo_screenheight()

self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))

self.master.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height,
    self.x_cordinate, self.y_cordinate))
print(self.x_cordinate)
print(self.y_cordinate)