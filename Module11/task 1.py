class publication:
    def __init__(self, name):
        self.name = name

class magazine(publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine name: {self.name}")
        print(f"Magazine chief editor: {self.chief_editor}")

class book(publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book name: {self.name}")
        print(f"Book author: {self.author}")
        print(f"Book pages: {self.pages}")

publications = []
publications.append(magazine("Donald Duck", "Aki Hyyppä"))
publications.append(book("Compartment No. 6", "Rosa Liksom", 192))

for pub in publications:
    print("---------------------")
    pub.print_information()

