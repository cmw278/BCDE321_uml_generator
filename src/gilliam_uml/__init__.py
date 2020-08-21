from .main import GilliamPrompt
from .controller import GilliamController


def launch_prompt():
    prompt = GilliamPrompt()
    prompt.prompt = '>->-> '
    prompt.cmdloop('\nWelcome to Gilliam the JS class diagram drawer. \nType'
                   + 'help or ? for a list of commands')
