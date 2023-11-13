# Import necessary PyQt modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Import custom Editor class and other required modules
from editor import Editor
import sys
import asyncio

# Import OpenAI and set API key and base URL
import openai

openai.api_key = "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"
openai.api_base = "http://localhost:1337/v1"

# Global variable for the main window
global window
               #
               #
               #
               #
#################################
               #
               #
               #
               #
               #
               #
               #
               #
               #
               #



# Define the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # Initialize UI and set flags
        self.init_ui()
        self.flag = False
        self.cnt = 0

    def init_ui(self):
        # Set up the main window UI elements
        self.app_name = "CodeAI"
        self.setWindowTitle(self.app_name)
        self.resize(1300, 900)

        # Apply styles from an external stylesheet
        self.setStyleSheet(open("./src/css/style.qss", "r").read())

        # Set font for the main window
        self.window_font = QFont("JetBrains Mono")
        self.window_font.setPointSize(12)
        self.setFont(self.window_font)

        # Set up the body of the main window
        self.set_up_body()
        self.set_widget()

        self.show()

    def get_editor(self, is_python_file=True):
        # Create an instance of the custom Editor class
        editor = Editor(self, is_python_file=is_python_file)
        return editor

    def set_widget(self):
        # Set up the editor widget
        self.editor = self.get_editor()
        self.text_view.addWidget(self.editor)
        self.editor.setText('')

    def add_text(self, txt):
        #####################################
        self.editor.setText(self.editor.text() + txt)

    def get_frame(self):
        # Create and configure a frame for styling purposes
        frame = QFrame()
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Plain)
        frame.setContentsMargins(0, 0, 0, 0)
        frame.setStyleSheet('''
            QFrame {
                background-color: #21252b;
                border-radius: 5px;
                border: none;
                padding: 5px;
                color: #D3D3D3;
            }
            QFrame:hover {
                color: white;
            }
        ''')
        return frame

    def generate_answer(self, txt):
        # Generate code completion using OpenAI Chat API
        print(txt)
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": txt}],
        )
        # Extract and append generated code to the editor
        code = chat_completion.choices[0].message.content
        print(code.split('```')[1][7:])
        self.add_text(code.split('```')[1][6:])

    def generate_text(self):
        #####################################
        q = self.input_field.text()
        self.input_field.clear()
        print(q)
        self.generate_answer(q)

    def set_up_body(self):
        #####################################
        body_frame = QFrame()
        body_frame.setFrameShape(QFrame.NoFrame)
        body_frame.setFrameShadow(QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0, 0)
        body_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body = QVBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        body_frame.setLayout(body)

        #####################################
        self.text_view = QHBoxLayout()
        self.text_view.setContentsMargins(0, 0, 0, 0)
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont('JetBrains Mono', 10))
        self.input_field.setStyleSheet('''
                    QLineEdit {
                        border-radius: 5px;
                        border: 2px solid white;
                        margin-left:20px;
                        margin-right:20px;
                        margin-bottom:20px;
                        height: 100px;
                    }
                ''')
        self.input_field.returnPressed.connect(self.generate_text)
        body.addLayout(self.text_view)
        body.addWidget(self.input_field)
        body_frame.setLayout(body)

        # Set the central widget for the main window
        self.setCentralWidget(body_frame)


# Entry point for the application
if __name__ == '__main__':
    # Create the application instance, main window, and run the application
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
