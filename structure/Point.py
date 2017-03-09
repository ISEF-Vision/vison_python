class Point:
    
    def __init__(self):
        self.x = 0;
        self.y = 0;

    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Check Point is Available on Image
    def assert_point(self,width,height):
        return (self.x > 0 and self.x < width) and (self.y > 0 and self.y < height)