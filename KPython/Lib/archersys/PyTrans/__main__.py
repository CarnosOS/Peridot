import string, os, cmd
class Translator(cmd.Cmd):
  def __init__(self):
     cmd.Cmd.__init__(self)
     self.pirate = {}
     self.pirate['sir'] = 'matey'
     self.pirate["hello"] = "avast"
     self.pirate["are"] = "be"
     self.pirate['hotel'] = 'fleabag inn'
     self.pirate['student'] = 'swabbie'
     self.pirate['boy'] = 'matey'
     self.pirate['restaurant'] = 'galley'
     self.pirate['you'] = 'ye'
     self.intro = "PyTrans Translator"
     self.prompt = "Language:>"
  def do_Pirate(self, arg):
      sentence = input("Please enter a sentence in English")
      
      psentence = []
      words = sentence.split()
      for aword in words:
         if aword in self.pirate:
             psentence.append(self.pirate[aword])
         else:
             psentence.append(aword)

      print(" ".join(psentence))
transl = Translator()
transl.cmdloop()