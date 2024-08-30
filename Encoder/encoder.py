"""
Encoder library for Raspberry Pi for measuring quadrature encoded signals.
created by Mivallion <mivallion@gmail.com>
Version 1.0 - 01 April 2020 - initial release - @mivallion
Version 1.1 - 15 May   2020 - fixed module import - @mivallion
Version 1.2 - 30 April 2024 - Added minor features - @CAP1Sup
"""

import RPi.GPIO as GPIO

class Encoder(object):
    """
    Encoder class allows to work with rotary encoder
    which connected via two pins: A and B. Pins are labelled
    in BCM mode by default, but mode can be specified
    Works only on interrupts because all RPi pins allow that.
    This library is a simple port of the Arduino Encoder library
    (https://github.com/PaulStoffregen/Encoder)
    """
    def __init__(self, A, B, mode=GPIO.BCM):
        GPIO.setmode(mode)
        GPIO.setup(A, GPIO.IN)
        GPIO.setup(B, GPIO.IN)
        self.A = A
        self.B = B
        self.pos = 0
        self.state = 0
        if GPIO.input(A):
            self.state |= 1
        if GPIO.input(B):
            self.state |= 2
        GPIO.add_event_detect(A, GPIO.BOTH, callback=self.__update)
        GPIO.add_event_detect(B, GPIO.BOTH, callback=self.__update)

    """
    update() calling every time when value on A or B pins changes.
    It updates the current position based on previous and current states
    of the rotary encoder.

    Channel is an optional parameter that is used by some GPIO libraries
    to specify which channel triggered the event. It is not used in this
    library, but it is still required in the function definition.
    """
    def __update(self, channel=None):
        state = self.state & 3
        if GPIO.input(self.A):
            state |= 4
        if GPIO.input(self.B):
            state |= 8

        self.state = state >> 2

        if state == 1 or state == 7 or state == 8 or state == 14:
            self.pos += 1
        elif state == 2 or state == 4 or state == 11 or state == 13:
            self.pos -= 1
        elif state == 3 or state == 12:
            self.pos += 2
        elif state == 6 or state == 9:
            self.pos -= 2

    """
    read() simply returns the current position of the rotary encoder.
    """
    def read(self):
        return self.pos

    """
    write() sets the position to a specified (integer) value
    """
    def write(self, value: int):
        try:
            self.pos = int(value)
        except ValueError:
            raise ValueError("Position must be an integer")
