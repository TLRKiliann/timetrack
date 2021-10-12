#!/usr/bin/python3
# -*- coding: utf-8 -*-


# To destroy or call MenuBar :

	self.mBar = MenuBar(self)
	self.mBar.pack(side=TOP, fill=X, expand=YES)

	self.mBar.destroy()


# To update second page :

	self.master.destroy()
	Application.__init__(self)
	self.showPatients()

# To access to an item of MenuBar (class)

    self.mBar.fileMenu
    self.mBar.me3
    self.mBar.me4
    self.mBar.meSoins
    self.mBar.meTtt
    self.mBar.meBmi
    self.mBar.meVmed
    self.mBar.mePrint
    self.mBar(self)