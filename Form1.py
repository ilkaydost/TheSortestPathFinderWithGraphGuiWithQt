# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ilkaydost/Desktop/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QPen, QColor, QFont ,QBrush
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsItem
from PyQt5.QtCore import Qt
import ShortestPath
import pyqtgraph as pg
import random

##I create object form Dijkstra Algorithm to use futher ın my code.
g = ShortestPath.Graph()

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(925, 439)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        ## I used QGraphichView for visualize the nodes.
        # For visualizing I need to QGrahicsScene which is draw shapes because of this
        # I added QGraphicsScene

        self.Graph_graphics = QtWidgets.QGraphicsView(Form)
        self.Graph_graphics.setAutoFillBackground(True)
        self.Graph_graphics.setObjectName("Graph_graphics")
        self.gridLayout.addWidget(self.Graph_graphics, 3, 0, 1, 1)
        self.Graph_graphicsScene = QtWidgets.QGraphicsScene(self.Graph_graphics)

        self.label_Graph = QtWidgets.QLabel(Form)
        self.label_Graph.setObjectName("label_Graph")
        self.gridLayout.addWidget(self.label_Graph, 2, 0, 1, 1)

        self.Terminal_Text = QtWidgets.QTextEdit(Form)
        self.Terminal_Text.setObjectName("Terminal_Text")
        self.gridLayout.addWidget(self.Terminal_Text, 6, 0, 1, 1)

        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 5, 0, 1, 1)
        self.line_vertical = QtWidgets.QFrame(Form)
        self.line_vertical.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("line_vertical")
        self.gridLayout.addWidget(self.line_vertical, 4, 0, 1, 2)
        self.line_horizontal = QtWidgets.QFrame(Form)
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("line_horizontal")
        self.gridLayout.addWidget(self.line_horizontal, 1, 1, 3, 1)
        self.line_horizontal_2 = QtWidgets.QFrame(Form)
        self.line_horizontal_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_horizontal_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal_2.setObjectName("line_horizontal_2")
        self.gridLayout.addWidget(self.line_horizontal_2, 5, 1, 2, 1)
        self.ShortPath = QtWidgets.QGridLayout()
        self.ShortPath.setObjectName("ShortPath")
        self.label_Source = QtWidgets.QLabel(Form)
        self.label_Source.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_Source.setObjectName("label_Source")
        self.ShortPath.addWidget(self.label_Source, 1, 1, 1, 1)
        self.pushButton_Run = QtWidgets.QPushButton(Form)
        self.pushButton_Run.setObjectName("pushButton_Run")

        ## I gave action when we press RUN button after than I added func. which is name run
        self.pushButton_Run.clicked.connect(self.run)

        self.ShortPath.addWidget(self.pushButton_Run, 2, 0, 1, 1)
        self.lineEdit_Source = QtWidgets.QLineEdit(Form)
        self.lineEdit_Source.setObjectName("lineEdit_Source")
        self.ShortPath.addWidget(self.lineEdit_Source, 2, 1, 1, 1)

        ## This lineEdit get written values and putting OnChangedSource func.
        self.lineEdit_Source.textChanged[str].connect(self.OnChangedSource)

        self.lineEdit_Destination = QtWidgets.QLineEdit(Form)
        self.lineEdit_Destination.setObjectName("lineEdit_Destination")
        self.ShortPath.addWidget(self.lineEdit_Destination, 2, 2, 1, 1)
        self.label_ShortestPath = QtWidgets.QLabel(Form)
        self.label_ShortestPath.setObjectName("label_ShortestPath")
        self.ShortPath.addWidget(self.label_ShortestPath, 0, 0, 1, 1)
        self.label_Dest = QtWidgets.QLabel(Form)
        self.label_Dest.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_Dest.setObjectName("label_Dest")
        self.ShortPath.addWidget(self.label_Dest, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.ShortPath, 6, 2, 1, 1)
        self.ContructNode = QtWidgets.QGridLayout()
        self.ContructNode.setContentsMargins(-1, -1, 0, -1)
        self.ContructNode.setSpacing(1)
        self.ContructNode.setObjectName("ContructNode")
        self.label_Weight = QtWidgets.QLabel(Form)
        self.label_Weight.setObjectName("label_Weight")
        self.ContructNode.addWidget(self.label_Weight, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushbutton_ConnectNode = QtWidgets.QPushButton(Form)
        self.pushbutton_ConnectNode.setObjectName("pushbutton_ConnectNode")
        self.ContructNode.addWidget(self.pushbutton_ConnectNode, 4, 0, 1, 1)

        ##This is another button to connect nodes from GUI
        self.pushbutton_ConnectNode.clicked.connect(self.connectNode)

        self.PushButton_AddNode = QtWidgets.QPushButton(Form)
        self.PushButton_AddNode.setObjectName("PushButton_AddNode")
        self.ContructNode.addWidget(self.PushButton_AddNode, 3, 0, 1, 1)

        ##This button added node when we pressed button and putting buttonClicked func.
        self.PushButton_AddNode.clicked.connect(self.buttonClicked)

        self.LineEdit_Adjacency = QtWidgets.QLineEdit(Form)
        self.LineEdit_Adjacency.setObjectName("LineEdit_Adjacency")
        self.ContructNode.addWidget(self.LineEdit_Adjacency, 4, 1, 1, 1)

        ##This LineEdit takes Adjancency nodes form GUI
        self.LineEdit_Adjacency.textChanged[str].connect(self.onChanged)

        self.label_Adj = QtWidgets.QLabel(Form)
        self.label_Adj.setObjectName("label_Adj")
        self.ContructNode.addWidget(self.label_Adj, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.lineEdit_Weight = QtWidgets.QLineEdit(Form)
        self.lineEdit_Weight.setObjectName("lineEdit_Weight")
        self.ContructNode.addWidget(self.lineEdit_Weight, 4, 2, 1, 1)

        ##This LineEdit takes Weight(Distance) value from GUI
        self.lineEdit_Weight.textChanged[str].connect(self.OnChangedWeigh)

        self.label_ConstructNode = QtWidgets.QLabel(Form)
        self.label_ConstructNode.setObjectName("label_ConstructNode")
        self.ContructNode.addWidget(self.label_ConstructNode, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.ContructNode, 3, 2, 1, 1)

        ##These are my data attributes so I used my algorithm. And Firstly I implemented

        self.nodeId = -1
        self.strNodeId = ""
        self.AdjText = ""
        self.WeightText = ""
        self.SourceText = ""

        ##!! These are not work because I couldn't finished my project properly!!
        self.DestinationText = ""
        self.x = ""
        self.startx  = 0
        self.starty = 0
        self.endx = 0
        self.endy = 0

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Shortest Path"))
        self.label_Graph.setText(_translate("Form", "GRAPH"))
        self.label_result.setText(_translate("Form", "RESULT"))
        self.label_Source.setText(_translate("Form", "Source"))
        self.pushButton_Run.setText(_translate("Form", "RUN"))
        self.label_ShortestPath.setText(_translate("Form", "The Shortest Path"))
        self.label_Dest.setText(_translate("Form", "Destination"))
        self.label_Weight.setText(_translate("Form", "Weight"))
        self.pushbutton_ConnectNode.setText(_translate("Form", "Connect Node"))
        self.PushButton_AddNode.setText(_translate("Form", "Add Node"))
        self.label_Adj.setText(_translate("Form", "Adjacency"))
        self.label_ConstructNode.setText(_translate("Form", "Construct Node"))

    ##ButtonClicked Func. works with add node button. When we press ADD NODE button we adding nodes.
    #Actually our program works with this func. We taking "add_node" func. from ShortestPath.py
    #Then We increase our NodeId beacause we need to create another name node
    #I used str format because ShortestPath.py works with str in name not values.
    #I used flag for creating another nodes
    #In If statement I used flag to creating another nodes
    #I used random module for giving coordinates randomly in beginning.(If I had a time I will Integrate with mouse and another nodes)
    #Then, I add line and Eclipse for using GraphicsScene which is I created of beginning of the code.
    #After, I used setScene func. to visualize in Main Frame
    #Later, I increase flag to break If statement and another nodes.

    def buttonClicked(self):

        self.nodeId += 1
        g.add_node(str(self.nodeId))
        self.flag = -1


        if self.flag < self.nodeId:
            self.x1 = random.randint(1, 50)
            self.x2 = random.randint(1, 30)
            self.y1 = random.randint(30, 40)
            self.y2 = random.randint(30, 40)

            self.Graph_graphicsScene.addLine(self.x1,self.y1,self.x2,self.y2)
            self.Graph_graphicsScene.addEllipse(self.x1,self.y1,self.x2,self.y2)
            self.Graph_graphics.setScene(self.Graph_graphicsScene)
            self.Graph_graphics.show()
            self.Graph_graphics.update()
            self.flag += 1

    ##ConnectNode fun. works with Conncet node pushbutton in GUI.
    #After pressed button,I give value nodeID to lastNode because I don't want to any confusion. I have to ın private but I did'nt managed time.
    #Then, I call ShortestPath.py to make connection between nodes. In this node I give WeightText which is write ın GUI.
    #I try to print terminal screen but I couldn't.

    def connectNode(self):
        self.lastNode = self.nodeId
        g.add_edge(str(self.AdjText), str(self.lastNode), int(self.WeightText))
        print("Adj. to:",self.AdjText,"Last Node from:" ,self.lastNode, "Weight: ",self.WeightText)
        self.Terminal_Text.setText(print("Adj. to:",self.AdjText,"Last Node from:" ,self.lastNode, "Weight: ",self.WeightText))

    ##I take text from GUI
    def onChanged(self):
        self.AdjText = self.LineEdit_Adjacency.text()
        return self.AdjText

    ##I take text from GUI
    def OnChangedWeigh(self):
        self.WeightText = self.lineEdit_Weight.text()
        return self.WeightText

    ##I take text from GUI
    def OnChangedSource(self):
        self.SourceText = self.lineEdit_Source.text()
        return self.SourceText

    ##In run func. I writte console output to Result section ın GUI.
    #My result from ShortestPath.py use dict. because of this I convert string format.
    #Later,I wrote result using Text.append func.
    def run(self):
        a = ShortestPath.dijsktra(g,str(self.SourceText))
        d = json.dumps(a)
        self.Terminal_Text.append(d)

    ##These both Mouse Event doesn't work because I didn't finished my project.
    def mousePressEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()

    def mouseReleaseEvent(self, event):
        self.x2 = event.x()
        self.y2 = event.y()
