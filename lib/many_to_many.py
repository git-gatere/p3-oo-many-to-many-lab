class Author:
    def __init__(self, name):
        self.name = name
        self.total_author_royalties = 0


    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.total_author_royalties = self.total_author_royalties + royalties
        return contract
    
    def total_royalties(self):
        return self.total_author_royalties


class Book:
    def __init__(self, title):
        self.title = title
    
    def books(self):
        pass


class Contract:
    all = []
    def __init__(self, author, book, date, royalties) -> None:
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Author must be an instance of author")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book must be an instace of book")
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Date must be a string")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Royalties must be an integer")
        
        Contract.all.append(self)
    


    