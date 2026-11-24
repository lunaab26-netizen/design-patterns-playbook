"""
Facade

Intent: give a complex subsystem one small, coherent entry point, so most callers never touch its internals.

Category: Structural
"""

class AudioExtractor:
    def extract(self, path): return f"audio<{path}>"

class CodecFactory:
    def for_format(self, fmt): return f"codec:{fmt}"

class Encoder:
    def __init__(self, codec): self.codec = codec
    def encode(self, audio): return f"{self.codec}|{audio}"

class VideoConverter:                      # the facade
    def convert(self, path: str, fmt: str) -> str:
        audio = AudioExtractor().extract(path)
        codec = CodecFactory().for_format(fmt)
        return Encoder(codec).encode(audio)

# caller sees one method instead of three collaborating classes
print(VideoConverter().convert("talk.mp4", "ogg"))
