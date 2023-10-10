class g_Father():
        surName=" "
        habbits=" "
        attitude=" "
        def __init__(self,surname,habbits,attitude):
                self.surName=surname
                self.habbits=habbits
                self.attitude=attitude
class father():
        fname=" "
        color=" "
        skill=" "
        def __init__(self,fname,color,skill):
                self.fname=fname
                self.color=color
                self.skill=skill
class son(g_Father,father):
        name= " "
        kind=" "
        bold= " "
        def __init__(self,surname,habbits,attitude,fname,color,skill,kind,bold):
                g_Father.__init__(self,surname,habbits,attitude,)
                father.__init__(self,fname,color,skill)
                self.name=self.surName+self.fname
                self.kind=kind
                self.bold=bold
        def display(self):
                print("Son Name is:",self.name)
                print("Son Kind is:",self.kind)
                print("Son Bold is:",self.bold)
                print("Son Habbits are:",self.habbits)
                print("Son Attitude is:",self.attitude)
                print("Son Color is:",self.color)
                print("Son Skill is:",self.skill)
s=son("Sandhinti","cricket,reading","good"," Raja Shaker","White","Talentade","Honest","False")
s.display()
