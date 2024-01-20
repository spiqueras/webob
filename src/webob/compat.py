# flake8: noqa

from cgi import FieldStorage as _cgi_FieldStorage
import tempfile


# Various different FieldStorage work-arounds required on Python 3.x
class cgi_FieldStorage(_cgi_FieldStorage):  # pragma: no cover
    def __repr__(self):
        """monkey patch for FieldStorage.__repr__

        Unbelievably, the default __repr__ on FieldStorage reads
        the entire file content instead of being sane about it.
        This is a simple replacement that doesn't do that
        """

        if self.file:
            return f"FieldStorage({self.name!r}, {self.filename!r})"

        return f"FieldStorage({self.name!r}, {self.filename!r}, {self.value!r})"

    # Work around https://bugs.python.org/issue27777
    def make_file(self):
        if self._binary_file or self.length >= 0:
            return tempfile.TemporaryFile("wb+")
        else:
            return tempfile.TemporaryFile("w+", encoding=self.encoding, newline="\n")
