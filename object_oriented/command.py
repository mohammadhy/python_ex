class screen(object):
    def __init__(self, text= ''):
        self.text = text 
        self.clip_board = ''

    def cut(self, start=0, end=0):
        self.clip_board = self.text[start:end]
        self.text = self.text[:start] + self.text[end:]


    def paste(self, offset=0):
        self.text = self.text[:offset] + self.clip_board


    def clear_clipborad(self):
        self.clip_board = ''


    def lengh(self):
        return len(self.text)

    def __str__(self):
        return self.text


class screencommand:
    def __init__(self, screen):
        self.screen = screen
        self.last_state = screen.text

    def execute(self):
        pass

    def undo(self):
        pass


class cutcommand(screencommand):
    def __init__(self, screen, start=0, end=0):
        super().__init__(screen)
        self.start = start
        self.end = end

    def execute(self):
        self.screen.cut(start=self.start , end=self.end)

    def undo (self):
        self.screen.clear_clipborad()
        self.screen.text = self.last_state


    
class pastecommand(screencommand):
    def __init__(self, screen, offset=0):
        super().__init__(screen)
        self.offset = offset

    def execute(self):
        self.screen.paste(offset=self.offset)

    def undo(self):
        self.screen.clear_clipborad()
        self.screen.text = self.last_state


class screeninvoker:
    def __init__(self):
        self.history = []


    def store_and_run(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


matn = screen('salam b hame ')
matn.__str__()
cut = cutcommand(matn,start= 7,end =  15)
client = screeninvoker()
client.store_and_run(cut)
matn.__str__()

