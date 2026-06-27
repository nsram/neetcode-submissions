class TextProcessor:
    # Implement method overloading for format_text method
    pass
    def format_text(self,a: str, b: str = "") -> str:
        if b=="":
            return a.upper()
        else:
            return a + b



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
