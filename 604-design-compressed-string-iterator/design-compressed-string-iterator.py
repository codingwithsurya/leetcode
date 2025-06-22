class StringIterator:
    def __init__(self, compressedString: str):
        self.uncompressed = []
        i, n = 0, len(compressedString)
        while i < n:
            ch = compressedString[i]
            i += 1
            # grab the full integer
            start = i
            while i < n and compressedString[i].isdigit():
                i += 1
            count = int(compressedString[start:i])
            self.uncompressed.append(ch * count)
        self.uncompressed = "".join(self.uncompressed)
        self.idx = -1

    def next(self) -> str:
        self.idx += 1
        return self.uncompressed[self.idx] if self.idx < len(self.uncompressed) else ' '

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.uncompressed)