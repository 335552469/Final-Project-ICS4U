class Camera(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.obj = []

    def moveX(self, speed):
        self.x += speed
        for i in self.obj:
            i[0] -= speed

    def moveY(self, speed):
        self.y += speed
        for i in self.obj:
            i[1] -= speed