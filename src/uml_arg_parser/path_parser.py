from pathlib import Path
import logging


class PathParser:
    """Parse selected file paths into memory using automatic directory
    traversal.
    """
    log = logging.getLogger('PathParser')

    def __init__(self):
        self.log.debug('Initialising PathParser')
        self.reset()

    def reset(self) -> None:
        """Reset PathParser to initial state.
        """
        self.log.debug('Reset command issued')
        self.paths = set()
        self.roots = set()

    def load(self, target: str, append: bool = True) -> None:
        """Scan and load target path into memory.

        ---
        Required Arguments:

        `[0] target: str`
        > The target file or directory to scan.

        ---
        Optional Arguments:

        `[1] append: bool`
        > Set to `False` to overwrite existing list of files (default: `True`)
        """
        self.log.debug('Loading path: %s' % target)
        if not append:
            self.log.debug('Overwriting path list')
            self.reset()
        root_path = Path(target)
        new_paths = self.scan_path(root_path)
        self.paths |= new_paths
        self.log.debug('Added %s paths to memory' % len(new_paths))
        self.roots.add(root_path)

    def scan_path(self, path: Path) -> set:
        """Scan a provided Path recursively, adding all files found to memory.

        ---
        Required Arguments:

        `[0] path: Path`
        > The path to scan.

        ---
        Returns a set containing discovered paths.
        """
        new_paths = set()
        if path.is_dir():
            new_paths = set(
                [self.scan_path(next_path) for next_path in path.iterdir()])
        else:
            new_paths.add(path)
        return new_paths

    def get_list(self) -> list:
        """Retrieve a list of files that have been found while scanning.
        """
        return list(self.paths)

    def filter_list(self, extension: str) -> list:
        """Returns a list of files with the required extension.

        ---
        Required Arguments:

        `[0] extension: str`
        > The extension to filter by.
        """
        return [path for path in self.paths if Path.suffix == extension]
