import sys
from cmd import Cmd
from .controller import GilliamController


class GilliamPrompt(Cmd):
    doc_header = "Here are the list of commands in help.\n To get help on a "\
     "command, enter 'help' followed by command name'."

    def do_help_list(self, arg):
        """Enter 'help_list to see a list of all the commands in help """ \
          """and what they do."""
        print("analyzer\t\tEnter 'analyzer' to analysis the selected file.\n"
              "\ndraw\t\tEnter 'draw' to draw the selected file.\n"
              "\nhelp_list\t\tEnter 'help_list to see a list of all the " +
              "commands in help and what they do.\n"
              "\nselect_file\t\tEnter 'select_file' to enter the file " +
              "path of the JavaScript file that requires a UML diagram.\n"
              "\nshut\t\tEnter 'shut y' To leave the program.")

    def do_select_file(self, arg):
        """Enter 'select_file' to enter the file path of the JavaScript"""\
         """file that requires a UML diagram """
        print('Enter the file path and file name of the file that ' +
              'requires analyzing')
        # call file opener

        file_name = arg
        #self.do_open_file(file_name)
        print(file_name)

    def do_open_file(self, file_name):
        print("Hi", file_name)
        file = open(file_name)
        print(file.read())

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
        if args == "y":
            sys.exit()
        else:
            print("Welcome back. Enter a command!")


if __name__ == '__main__':
    prompt = GilliamPrompt()
    prompt.prompt = '>->-> '
    prompt.cmdloop('\nWelcome to Gilliam the JS class diagram drawer.\
                    \nType help or ? for a list of commands')

