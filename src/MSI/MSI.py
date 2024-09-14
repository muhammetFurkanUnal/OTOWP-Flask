from .engine import PyWp

class MSI:
    
    def __init__(self):
        self.engine = PyWp()
        
    
    def sendMessage(self, message, groups):
        for group in groups:
            self.engine.send_message(group, message)

        
        