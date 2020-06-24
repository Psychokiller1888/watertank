import time

import machine

class Watertank:

	def __init__(self):
		self._emptySensor = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
		self._fullSensor = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
		self._relay = machine.Pin(5, machine.Pin.OUT)

		self._emptySensor.irq(handler=self.onEmpty, trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)
		self._fullSensor.irq(handler=self.onFull, trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)


	def onEmpty(self, pin: machine.Pin):
		if not pin.value():
			self._relay.off()
			time.sleep(0.5)


	def onFull(self, pin: machine.Pin):
		if pin.value():
			self._relay.on()
			time.sleep(0.5)


if __name__ == '__main__':
	Watertank()
