class Camera(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.obj = []

    def moveX(self, speed, dt):
        self.x += speed
        for i in self.obj:
            i[0] -= speed*dt

    def moveY(self, speed, dt):
        self.y += speed
        for i in self.obj:
            i[1] -= speed*dt