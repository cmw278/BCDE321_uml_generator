from graphviz_uml import GraphvizUML
import json
import gc


class GilliamController:
    def __init__(self):
        self._js_dict = None
        self._uml_generator = None

    def open_file(self, targetfile: str) -> None:
        """Load a file into memory and prepare it for generating a UML 2
        class diagram.

        ---
        Required Positional Arguments:

        `[0] targetfile: str`
        > The path to the file you wish to open. Can be
        a relative or absolute path.
        """
        file_ = open(targetfile)
        self._js_dict = json.load(file_)

    def run_analysis(self):
        """Generate the DOT formatted string for the currently loaded file.

        ---
        `returns -> str`
        > The DOT formatted string.
        """
        self._get_uml_generator()
        return str(self._uml_generator)


    def save_file(self, *, filename: str = None,
                  directory: str = None, format: str = 'png') -> str:
        """Save the generated UML 2 class diagram.

        ---
        `returns -> str`
        > The path the file was saved to.

        ---
        Optional Keyword Arguments:

        `filename: str`
        > The destination filename (without the extension).
        Defaults to the name of the directory or file the UML is generated
        from.

        `directory: str`
        > The destination directory where output will be saved.
        Defaults to the current working directory.

        `format: str`
        > The desired file format of the generated UML.
        Common formats include: png, pdf, svg, jpeg, jpg, bmp, gif, tiff, tif,
        fig, dot_json, and json
        Defaults to png.
        """
        self._get_uml_generator()
        self._uml_generator.render(
            filename=filename,
            directory=directory,
            format=format,
            cleanup=True
        )

    def view_uml(self, *, filename: str = None,
                  directory: str = None, format: str = 'png') -> str:
        """Saves the generated UML 2 class diagram and opens the resulting
        file for preview.

        ---
        `returns -> str`
        > The path the file was saved to.

        ---
        Optional Keyword Arguments:

        `filename: str`
        > The destination filename (without the extension).
        Defaults to the name of the directory or file the UML is generated
        from.

        `directory: str`
        > The destination directory where output will be saved.
        Defaults to the current working directory.

        `format: str`
        > The desired file format of the generated UML.
        Common formats include: png, pdf, svg, jpeg, jpg, bmp, gif, tiff, tif,
        fig, dot_json, and json.
        Defaults to png.
        """
        self._get_uml_generator()
        self._uml_generator.view(
            filename=filename,
            directory=directory,
            format=format,
            cleanup=True
        )

    def _get_uml_generator(self) -> None:
        """Intantiate `GraphvizUML` class using stored `dict`.

        ---
        Will create an instance of GraphvizUML using `self._js_dict`. If
        `self._js_dict` is unset, an `AssertionError` will be raised.

        The GraphvizUML instance will be stored in `self._uml_generator`.
        """
        assert self._js_dict is not None, """You must open a file before
        this operation can be performed.
        """
        self._uml_generator = GraphvizUML(self._js_dict)
