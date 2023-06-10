# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, UserUtteranceReverted

import random
import requests

initial_greets = [
    "Hey there!", 
    "Hello human!", 
    "Good day!"
]

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        events = [SessionStarted()]
        index = random.randint(0,len(initial_greets)-1)
        dispatcher.utter_message(initial_greets[index])
        
        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events

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

class JokeRequest(Action):

    def name(self) -> Text:
        return "joke_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = "https://dad-jokes.p.rapidapi.com/random/joke"

        headers = {
            "X-RapidAPI-Key": "43e9749900msh84826b981c67b03p17e368jsn435203284416",
            "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        jsonData = response.json()
        setup = jsonData["body"][0]["setup"]
        punchline = jsonData["body"][0]["punchline"]
        
        return [SlotSet("joke_setup", setup),SlotSet("joke_punchline", punchline)]



