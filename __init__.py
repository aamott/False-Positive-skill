from mycroft import MycroftSkill, intent_file_handler
import os
from pathlib import PurePath

class FalsePositive(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.filepath = "uninitialized_todavia"
        self.subdir = "not-wake-word/"


    def initialize(self):
        self.add_event('recognizer_loop:wakeword',
                       self.handle_listener_started)
        # self.add_event('recognizer_loop:record_end',
        #                self.handle_listener_ended)

    @intent_file_handler('false-positive.intent')
    def handle_false_positive(self, message):
        if os.path.exists(self.filepath):
            filename = os.path.basename(self.filepath)
            directory = os.path.dirname(self.filepath)
            parent_directory = PurePath(directory).parent.name + '/'
            if not os.path.isdir(parent_directory + self.subdir):
                os.mkdir(parent_directory + self.subdir)
            os.rename(self.filepath, parent_directory + self.subdir + filename)

            self.speak_dialog('false-positive')
        else:
            self.speak_dialog('no-recording')


    def handle_listener_started(self, message):
        if "filepath" in message.data:
            self.filepath = message.data.get("filepath")
        else:
            self.filepath = None

def create_skill():
    return FalsePositive()
