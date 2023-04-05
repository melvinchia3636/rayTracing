from vector import Vec3


class Color(Vec3):
    @classmethod
    def from_hex(cls, hex="#000000"):
        hex = hex.lstrip('#')
        return cls(*tuple(int(hex[i:i+2], 16)/255.0 for i in (0, 2, 4)))
