class Publication:
    def __init__(self, __title, __author):
        self.__author = __author
        self.__title = __title

    #setter functions

    def get_author(self):
        return "Author: " + self.__author

    def get_title(self):
        return "Title: " + self.__title

    #setter functions

    def set_author(self, newauthor):
        self.__author = newauthor

    def set_title(self, newtitle):
        self.__title = newtitle

    def display_info(self):
        print(self.get_title())
        print(self.get_author())

class Book(Publication):
    def __init__(self, __title, __author, __number_of_pages):
        super().__init__(__title , __author)
        self.__number_of_pages = __number_of_pages

    #getter functions    

    def get_author(self):
        return super().get_author() # Returns function in order for value to be not none (stuck here for a while)

    def get_title(self):
        return super().get_title()

    def get_number_of_pages(self):
        return "Number of pages: " + str(self.__number_of_pages)

    #setter functions

    def set_author(self, newauthor):
        super().set_author()

    def set_title(self, newtitle):
        super().set_title()

    def set_number_of_pages(self, newnumberofpages):
        if newnumberofpages <= 0: # checks if input is valid
            print("Number of pages must be positive")
        else:
            self.__number_of_pages = newnumberofpages

    def display_info(self):
        super().display_info()

class Magazine(Publication):
    def __init__(self, __title, __author, __issue_number):
        super().__init__(__title , __author)
        self.__issue_number = __issue_number

    #getter functions

    def get_author(self): 
        return super().get_author() 

    def get_title(self):
        return super().get_title()

    def get_issue_number(self):
        return "Issue Number: " + str(self.__issue_number)

    #setter functions

    def set_author(self, newauthor):
        super().set_author()

    def set_title(self, newtitle):
        super().set_title()

    def set_issue_number(self, newissuenumber):
        if newissuenumber <= 0: # checks if input is valid
            print("Issue number must be positive")
        else:
            self.__issue_number = newissuenumber

    def display_info(self):
        super().display_info()

#callouts

pub1 = Publication("Journal of Experimental Psychology","Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information")
pub1.display_info()

print("\nBook Information")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information")
mag1.display_info()
print(mag1.get_issue_number())
