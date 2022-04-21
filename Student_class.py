class Student:
    
    def __init__(self, ID, name, group_dynamic, leadership, english_writing_skill, programming_attitude, conflict_resolution_approach, interaction):
        self.ID = ID
        self.name = name
        self.group_dynamic = group_dynamic
        self.leadership = leadership
        self.english_writing_skill = english_writing_skill
        self.programming_attitude = programming_attitude
        self.conflict_resolution_approach = conflict_resolution_approach
        self.interaction = interaction

    def isExtrovert(self):
        if self.group_dynamic == "An EXTROVERT":
            return True
        return False

    def isLeader(self):
        if self.leadership == "A natural leader":
            return True
        return False

    def isManager(self):
        if self.leadership == "An effective manager":
            return True
        return False

    def toDict(self):
        dictionary_version = {
            "ID": self.ID,
            "name": self.name,
            "group_dynamic": self.group_dynamic,
            "leadership": self.leadership,
            "english_writing_skill": self.english_writing_skill,
            "programming_attitude": self.programming_attitude,
            "conflict_resolution_approach": self.conflict_resolution_approach,
            "interaction": self.interaction
        }
        return dictionary_version
