class Student:
    index_number: str
    name: str | None = None
    address: str | None = None
    gender: str | None = None
    date_of_birth: str | None = None  # Date
    parent_name: str | None = None
    contact_number: str | None = None
    grade: str | None = None

    def __int__(self, i, n, a, g, d, p, c, gr):
        self.index_number = i
        self.name = n
        self.address = a
        self.gender = g
        
