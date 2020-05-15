# Raspberry Pi Rotary Encoder Library

Encoder library for Raspberry Pi for measuring quadrature encoded signals.
### About
Encoder class allows to work with rotary encoder which connected via two pin A and B (EN11 for example). Works only on interrupts because all RPi pins allow that. This library is a simple port of the Arduino Encoder library (https://github.com/PaulStoffregen/Encoder)

### Installation
```sh
$ pip install Encoder
```

### Usage

To use it, you need to connect pins A and B and GND of the rotary encoder to two pins and GND of the Raspberry Pi, for example 24 and 10. Then just use it:
```python
import Encoder

enc = Encoder.Encoder(24, 10)
enc.read()
```

You can use two or more rotary encoders:
```python
import Encoder

enc_1 = Encoder.Encoder(24, 10)
enc_2 = Encoder.Encoder(25, 9)
```

### Note
If the encoder works in the wrong direction, for example, it reduces the position when turning clockwise, you just need to swap pins A and B in the code.

License
----

MIT
