from dot_formatter import DotArgument


class DotAttribute(DotArgument):

    def __str__(self):
        super_string = super().__str__()
        return '+ %s<br/>' % super_string
