from PyQt5.QtGui import *

from PyQt5.Qsci import *

from highlighting import HighlightTokens


class Editor(QsciScintilla):

    def __init__(self, main_window, parent=None, is_python_file=True):
        super(Editor, self).__init__(parent)

        self.main_window = main_window
        self._current_file_changed = False
        self.first_launch = True
        self.is_python_file = is_python_file
        self.setUtf8(True)
        self.window_font = QFont(
            "JetBrains Mono")
        self.window_font.setPointSize(12)
        self.setFont(self.window_font)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setIndentationGuides(True)
        self.setTabWidth(4)
        self.setIndentationsUseTabs(False)
        self.setAutoIndent(True)
        self.setCaretForegroundColor(QColor("#dedcdc"))
        self.setCaretLineVisible(True)
        self.setCaretWidth(2)
        self.setCaretLineBackgroundColor(QColor("#2c313c"))
        self.setEolMode(QsciScintilla.EolWindows)
        self.setEolVisibility(False)

        if self.is_python_file:
            self.pylexer = HighlightTokens(self)
            self.pylexer.setDefaultFont(self.window_font)
            self.__api = QsciAPIs(self.pylexer)
            self.setLexer(self.pylexer)
        else:
            self.setPaper(QColor("#282c34"))
            self.setColor(QColor("#abb2bf"))
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, "000")
        self.setMarginsForegroundColor(QColor("#ff888888"))
        self.setMarginsBackgroundColor(QColor("#282c34"))
        self.setMarginsFont(self.window_font)
