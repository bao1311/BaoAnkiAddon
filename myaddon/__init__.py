# mw ~ main window object
from aqt import  mw

from aqt.utils import showInfo, qconnect

from aqt.qt import *

def testFunction():
  # Get the total number of card inside Anki
  cardCount = mw.col.cardCount()
  showInfo("Card count: " + str(cardCount))
  # Try to find a due card
  card = mw.col.sched.getCard()
  if not card:
    # The current deck is done
    print("The deck is done! You have done a good job today")
  else:
    note = card.note()
    for (name,value) in note.items():
      note[name] = value + " new (Added by Bao addons"
  # Get card IDs for note with tag x
  ids = mw.col.find_cards("tag:x")

  res = ""
  # Print out all the question and answer of those ids
  for id in ids:
    card = mw.col.sched.getCard(id)
    question = card.question()
    answer = card.answer()
    res += question + answer
  showInfo("All the question and answer: ", res)




#mw mean main window
action = QAction("test",mw)

qconnect(action.triggered, testFunction)

mw.form.menuTools.addAction(action)