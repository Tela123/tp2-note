from datetime import datetime 

class Note:
    note_id=0
    def __init__(self,memo,balise):
        self.note_id=Note.note_id
        Note.note_id+=1
        self.memo=memo
        self.balise=balise
        self.date_creation=datetime.now()
    def correspondance(self, terme):
        return terme.lower() in self.memo or terme.lower() in self.balise
    
note=Note("ceci est une note cree","test")
print(note.correspondance("note"))

class Notebook:
    
    def __init__(self):
        self.notes=[]
    def Ajouter_note(self, memo,balise):
        self.notes.append(Note(memo,balise))
    def Consulter_note(self):
        for note in self.notes:
            print(f'id:{note.note_id}, memo:{note.memo}, balise:{note.balise}, date creation:{note.date_creation}')
    def Modifier_note(self,note_id, memo=None, balise=None):
        note_update=None
        for note in self.notes:
            if(note.note_id==note_id):
                note_update=note
                break
            if note_update:
                if memo:
                    self.memo=memo
                if balise:
                    self.balise=balise