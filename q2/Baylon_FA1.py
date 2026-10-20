class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if isinstance(number_of_pages, int) and not isinstance(number_of_pages, bool) and number_of_pages > 0:
            self.number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
            self.number_of_pages = None

    def display_info(self):
        super().display_info()
        if self.number_of_pages is not None:
            print("Number of pages:", self.number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.issue_number = issue_number
        else:
            print("The issue number must be positive.")
            self.issue_number = None

    def display_info(self):
        super().display_info()
        if self.issue_number is not None:
            print("Issue number:", self.issue_number)


# Create two Publication objects
publication1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)
publication2 = Publication(
    "The Science Journal",
    "John Smith"
)

# Create two Book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Invalid Book", "Unknown Author", 0)

# Create two Magazine objects
magazine1 = Magazine("National Geographic", "Various Authors", 202)
magazine2 = Magazine("Science Monthly", "Various Authors", 15)


# Display Publication information
print("Publication Information:")
publication1.display_info()
print()
publication2.display_info()
print()

# Display Book information
print("Book Information:")
book1.display_info()
print()
book2.display_info()
print()

# Display Magazine information
print("Magazine Information:")
magazine1.display_info()
print()
magazine2.display_info()
