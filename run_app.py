from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-418693047175-417800008789-418697978855-a95d69f4a6d97bfa986e31f60b29713a', #app verification token
							'xoxb-418693047175-417427144676-4PeWfc89vfTMgqYCyU1RoyXu', # bot verification token
							'KULD7DRrmrDNSGgfZ54VxjHQ', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))