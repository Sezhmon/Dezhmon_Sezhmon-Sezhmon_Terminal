import sys

class ConsoleRedirector:
    def __init__(self, label, scroll):
        self.label = label
        self.scroll = scroll

    def write(self, message):
        if message:
            self.label.text += message
            self.scroll.scroll_y = 0

    def flush(self):
        pass

def Setup_Terminal_Stdout(label, scroll):
    sys.stdout = ConsoleRedirector(label, scroll)