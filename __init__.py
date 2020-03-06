from mycroft import MycroftSkill, intent_file_handler
import os

class FalsePositive(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.filename = "uninitialized_todavia"
        self.subdir = "not-wake-word/"


    def initialize(self):
        self.add_event('recognizer_loop:record_begin',
                       self.handle_listener_started)
        # self.add_event('recognizer_loop:record_end',
        #                self.handle_listener_ended)

    @intent_file_handler('false-positive.intent')
    def handle_false_positive(self, message):
        #move file to subdirectory
        if os.path.exists(self.filepath)
            filename = os.path.basename(self.filepath)
            directory = os.path.dirname(self.filepath)
            if not isdir(filepath + self.subdir):
                os.mkdir(filepath + self.subdir)
            os.rename(self.filepath, self.filepath + self.subdir + filename)
            
            self.speak_dialog('false-positve.dialog')
        else:
            self.speak_dialog('no_recording.dialog')


    def handle_listener_started(self, message):
        if "filepath" in message:
            self.filepath = message.get("filepath")
