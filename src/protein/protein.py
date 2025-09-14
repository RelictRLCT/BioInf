class Protein:
    def __init__(self, desc: str, code: str):
        self.desc = desc
        self.code = code

    def __str__(self):
        return f"{self.desc}\n{self.code}"
