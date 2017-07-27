import threading

class Animation(threading.Thread):
    stopped = False
    def start(self, strip):
        raise NotImplementedError

    def stop(self):
        self.stopped = True

def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)