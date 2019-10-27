import enum
import io
import base64
from PIL import Image

class Resolution(enum.Enum):
    THUMBNAIL = 0
    STANDARD = 1
    ORIGIN = 2

class ImageOutput:
    def __init__(self, pillow_out):
        self.out = pillow_out
    
    def save(self, file_path):
        self.out.save(file_path, "JPEG")
        
    def show(self):
        self.out.show()

    def base64(self):
        with io.BytesIO() as buffer:
            self.out.save(buffer, 'JPEG')
            return base64.b64encode(buffer.getvalue()).decode()

class Resizer:
    def __init__(self, buffer=None, path=None):
        if buffer is not None:
            self.im = Image.open(buffer)
        elif path is not None:
            self.im = Image.open(path)

    def resolutionDict(self, resolution):
        res = Resolution.ORIGIN
        w = None
        h = None
        if resolution == "thumbnail":
            res = Resolution.THUMBNAIL
            w = 128
            h = 128
        elif resolution == "standard":
            res = Resolution.STANDARD
            w = 512
            h = 512
        return dict(resolution = res, w = w, h = h)

    def resize(self, w, h):
        self.out = self.im.resize((w, h))
        return self
    
    def output(self):
        return ImageOutput(self.out)
