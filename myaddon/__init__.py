# mw ~ main window object
from aqt import  mw

from aqt.utils import showInfo, qconnect

from aqt.qt import *

def testFunction():
  cardCount = mw.col.cardCount()
  showInfo("Card count: " + str(cardCount))


#mw mean main window
action = QAction("test",mw)

qconnect(action.triggered, testFunction)

mw.form.menuTools.addAction(action)