

class Box:

    width = 0
    height = 0
    bredth = 0

    def __init__(self,h,w,b):
        self.width = w
        self.bredth = b
        self.height = h
    
    # def __init__(self,len):
    #     self.height = self.bredth = self.width = len
    
    # def __init__(self):
    #     self.height = 0
    #     self.width = 0
    #     self.bredth = 0
    
    def volume(self):
        return self.width*self.height*self.bredth


class BoxWeight(Box):
    
    weight = 0

    def __init__(self,mass,width,height,bredth):
        super().__init__(height,width,bredth)
        self.weight = mass
        

    # def __init__(self,mass,len):
    #     super().__init__(len)
    #     self.weight = mass
        
    
    # def __init__(self):
    #     super().__init__(self)
    #     self.weight = 0
        

class Demo:

    box = BoxWeight(51,15,20,10)
    # cube = BoxWeight(41,5)
    # emptybox = BoxWeight()

    vol = box.volume()
    print("Volume of Box is: ",vol)
    print("Weight of Box is: ",box.weight)

    # vol = emptybox.volume()
    # print("Volume of EmptyBox is: ",vol)
    # print("Weight of EmptyBox is: ",emptybox.weight)

    # vol = cube.volume()
    # print("Volume of Cube is: ",vol)
    # print("Weight of Cube is: ",cube.weight)