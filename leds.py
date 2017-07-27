from flask import Flask, render_template, request, jsonify
from neopixel import *
import animations

# LED strip configuration:
LED_COUNT   = 60     # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

app=Flask(__name__)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

animation_list = {
	rainbow_cycle: 0
}

animation = None

def allColor(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
	strip.show()

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/set_color", methods=['POST'])
def set_color():
	rgb = request.get_json()
	if animation is not None:
		animation.stop()
		animation = None
	allColor(strip, Color(rgb['r'], rgb['g'], rgb['b']))
	return render_template('index.html'), 204

@app.route("/set_brightness", methods=['POST'])
def brightness():
	brightness = int(request.form['brightness'])
	strip.setBrightness(brightness)
	return 204

@app.route("/animation", methods=['GET', 'POST'])
def animation():
	if request.method = 'GET':
		return jsonify(animation_list)
	else:
		requested_animation = request.form['animation']
		if requested_animation == 'rainbow_cycle':
			animation = animations.rainbowcycle.RainbowCycle()
			animation.start()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
