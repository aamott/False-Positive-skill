from mycroft import MycroftSkill, intent_file_handler
from pathlib import Path
from os import scandir, remove
from os.path import basename
import shlex, subprocess #for executing in terminal
import copy
#os.path.basename
#os.remove delete file
#os.scandir return a list of filepaths

class CustomCommand:
   #phrase.           what the user wants to say(str)
   # command          bash command (str)
    def __init__(phrase, command):
        self.phrase = phrase
        self.command = command
        intent_file_handler(self.phrase, copy.deepcopy(handle_command))

    def handle_command(self, message):
        args = shlex.split(phrase)
        # if you had any custom input in message, you could add it through the message
        # for now, we'll just run the plain phrase
        self.task = subprocess.Popen(args)

#Note: Popen expects a list of strings. The first string is typically the program to be run, followed by its arguments. Sometimes when the command is complicated, it's convenient to use shlex.split to compose the list for you:
#import shlex 
#proc=subprocess.Popen(shlex.split())

class TerminalCommand(MycroftSkill): 
   def __init__(self): 
      MycroftSkill.__init__(self)
      # get all user's custom commands from a textbox in the settings page
#      usr_data = self.settings.get("custom commands")
#      if not usr_data:
#        usr_data = "launch firefox : firefox \n release the penguins : xpenguins"
#      # put all the settings in a dictionary so they can be searched
#        self.commands  = dict(p.split(' : ') for p in usr_data.split("\n"))
      self.commands = {}
      for i in range(1, 5):
          if self.settings.get("custom command " + str(i)):
              command = self.settings.get("custom command " + str(i)).split(" : ")
              self.commands[command[0]] = command[1]

      intents_dir = str(Path.cwd()) + "/skills/terminal-skill.aamott/vocab/en-us/"

      intents = ""
      with open(intents_dir + "all-commands.intent", 'r') as f:
        for intent in self.commands.keys():
           intents += intent + '\n'

        rewrite_file = not f.read() == intents

      if rewrite_file:
        with open(intents_dir + "all-commands.intent", 'w') as f:
            f.truncate()
            f.write(intents)
        
        
        
#      # do intent setup
#      path = Path.cwd()
#      intents_dir = str(path) + "/skills/terminal-skill.aamott/vocab/en-us"
#      intent_files = scandir(intents_dir)
#      command_keys = self.commands.keys()
#      #check for deleted commands
#      for file in intent_files:
#         if not str(basename(file).rstrip(".intent")) in command_keys:
#            remove(file)
#
#      intents = {}
#      #get just the intent filenames, no extensions
#      for intent in intent_files:
#          intents.append(basename(intent).rstrip(".intent"), )
#      for command in self.commands.keys():
#         if not command in intents: 
#            #name each file with the phrase
#            with open(command + '.intent', 'w') as f:
#               f.write(command)

      # initialize all commands
#      for p, c in self.commands.items():
#        intent_file_handler(p)
      

   @intent_file_handler("all-commands.intent")
   def handle_command(self, message):
     utterance = message.data["utterance"]
     command = None
     for command_phrase in self.commands.keys():
        if command_phrase in utterance:
            command = self.commands.get(command_phrase)
            break

     if command:
        args = shlex.split(command)
        # if you had any custom input in message, you could add it through the message
        # for now, we'll just run the plain phrase
        self.task = subprocess.Popen(args)
     else:
        pass

def create_skill():
    return TerminalCommand()
