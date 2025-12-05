class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
        print(f"Added book: {title} by {author}")

    def search(self, keyword):
        keyword = keyword.lower()
        results = [book for book in self.books
                   if keyword in book["title"].lower() or keyword in book["author"].lower()]
        return results
lib = Library()
lib.add_book("Clean Code", "Robert Martin")
lib.add_book("Code Complete", "Steve McConnell")
lib.add_book("The Pragmatic Programmer", "Andrew Hunt")
print("Search results for 'code':", lib.search("code"))
print("Search results for 'martin':", lib.search("martin"))
