# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
import random

# initial_greets = [
#     "Hey there!", 
#     "Hello human!", 
#     "Good day!"
# ]

# class ActionSessionStart(Action):
#     def name(self) -> Text:
#         return "action_session_start"

#     async def run(
#       self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
        
#         events = [SessionStarted()]
#         index = random.randint(0,len(initial_greets)-1)
#         #dispatcher.utter_message(initial_greets[index])
        
#         # an `action_listen` should be added at the end as a user message follows
#         events.append(ActionExecuted("action_listen"))

#         return events

# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""

#     def name(self) -> Text:
#         return "action_default_fallback"

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_default")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]

class SetAlreadyScared(Action):

  def name(self) -> Text:
      return "set_already_scared"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:
  
        return[SlotSet("previously_scared", True)]
  
class SetAlreadySurprised(Action):

  def name(self) -> Text:
      return "set_already_surprised"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:
  
        return[SlotSet("previously_surprised", True)]