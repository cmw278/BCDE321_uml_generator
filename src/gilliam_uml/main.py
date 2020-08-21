import sys
from cmd import Cmd
from .controller import GilliamController


class GilliamPrompt(Cmd):
    doc_header = "Here are the list of commands in help.\n To get help on a command enter 'help" \
                 " followed by command name'."

    def do_help_list(self, arg):
        """Enter 'help_list to see a list of all the commands in help and what they do."""
        print(
            "analyzer\n\tEnter 'analyzer' to analysis the selected file.\n"
            "\ndraw\n\tEnter 'draw' to draw the selected file.\n"
            "\nhelp_list\n\tEnter 'help_list to see a list of all the commands in help and what they do.\n"
            "\nselect_file\n\tEnter 'select_file' to enter the file path of the JavaScript file that" +
            "requires a UML diagram\n "
            "\nshut\n\tEnter 'shut y' To leave the program.")

    def do_select_file(self, arg):
        """Enter 'select_file' to enter the file path of the JavaScript file that requires a UML diagram """
        print('Hello')
        # call file opener

    def do_analyzer(self, arg):
        """Enter 'analyzer' to analysis the selected file."""
        print('Running analyzer')
        # call file analyzer

    def do_draw(self, arg):
        """Enter 'draw' to draw the selected file."""
        print("Drawing UML diagram")
        # call file drawer

    def do_shut(self, args):
        """ Enter 'shut y' To leave the program."""
        print("Enter' Confirm Y' to close program. To leave program open enter 'Confirm N")

    def do_Confirm(self, args):
        """Close the program."""
        if args == "Y":
            sys.exit()
        else:
            print("Welcome back. Enter a command!")


if __name__ == '__main__':
    prompt = GilliamPrompt()
    prompt.prompt = '>->-> '
    prompt.cmdloop(
        '\nWelcome to Gilliam the JS class diagram drawer. \nType help or ? for a list of commands')
