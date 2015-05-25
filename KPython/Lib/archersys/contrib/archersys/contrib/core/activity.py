import cmd
'''
Created on May 22, 2015

@author: Weldon Henson

'''
class AbstractActivityKernel(cmd.Cmd):
    def __init__(self,prompt,intro):
        cmd.Cmd.__init__(self)
        self.prompt = prompt
        self.intro = intro
        