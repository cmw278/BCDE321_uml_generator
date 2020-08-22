from graphviz import Source, FORMATS
from dot_formatter import DotFormatter


class GraphvizUML(Source, DotFormatter):
    """A UML rendering engine that wraps dot_formatter.DotFormatter and
    graphviz.Source to render the output in one of the image formats
    supported by graphviz.

    GraphvizUML uses multiple inheritance, so an instance can be interacted
    using both the DotFormatter API AND the graphviz.Source API, although
    some behaviour is altered.

    All altered behaviour is documented in the method docstrings.
    """

    def __init__(self, system_dict: dict, *, template_path: str = None,
                 filename: str = None, directory: str = None,
                 format: str = 'png'):
        """Creates a GraphvizUML instance that may be interacted with using
        the API of graphviz.Source AND dot_formatter.DotFormatter.
        DotFormatter is instantiated first, then cast as string to instantiate
        Source.

        ---
        Required Positional Arguments:

        `[0] system_dict: dict`
        > A dictionary representation of the system you are creating a UML
        model for.

        ---
        Optional Keyword Arguments:

        `template_path: str`
        > Path to a custom DOT file template, used when casting DotFormatter
        as a string.

        `filename: str`
        > Filename for saving the output. Defaults to
        `system_dict['folder_name']`.

        `directory: str`
        > (Sub)directory for source saving and rendering.

        `format: str`
        > Rendering output format ('pdf', 'png', …). Defaults
        to `png` (different behaviour from graphviz.Source).
        """
        assert (format in FORMATS,
                '%s format: is not supported. Format must be one of: [ %s ]'
                % (format, ', '.join(FORMATS)))
        DotFormatter.__init__(self, system_dict, template_path=template_path)
        Source.__init__(self, str(self),
                        filename=self.name if filename is None else filename,
                        directory=directory, format=format)

    def view(self, *, filename: str = None, directory: str = None,
             cleanup: bool = True, format: str = None) -> str:
        """Save the UML diagram to file, open the result in a viewer.

        ---
        `returns: str`
        > Returns the filepath where the output was saved.

        ---
        Optional Keyword Arguments:

        `filename: str`
        > Filename for saving the source (defaults to name + '.gv')

        `directory: str`
        > (Sub)directory for source saving and rendering.

        `cleanup: bool`
        > Delete the source file after rendering (Defaults to True).

        `format: str`
        > The output format used for rendering (pdf, png, etc.).
        """
        return Source.render(self, view=True, filename=filename,
                      directory=directory, cleanup=cleanup, format=format)
