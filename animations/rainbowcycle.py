import animation
import time

class RainbowCycle(animation.Animation):
    iterations = 5
    wait = 20
    def start(self, strip):
        while not self.stop:
            for j in range(256 * self.iterations):
                for i in range(strip.numPixels()):
                    strip.setPixelColor(i, animation.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
                strip.show()
                time.sleep(self.wait / 1000.0)
                