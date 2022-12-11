from models.book import *

desc1 = "Empire in Black and Gold follows the Beetle Kinden Stenwold Maker and his attempts to convince the rulers of his home-city of Collegium that there is a vast and bloodthirsty enemy coming from the North to conquer them: the Wasp Empire."

desc2 = "Two hundred years after migrating into space, mankind is in turmoil. When a reluctant ship's captain and washed-up detective find themselves involved in the case of a missing girl, what they discover brings our solar system to the brink of civil war, and exposes the greatest conspiracy in human history."

desc3 = "Detective John Rebus: His city is being terrorized by a baffling series of murders…and he's tied to a maniac by an invisible knot of blood. Once John Rebus served in Britain's elite SAS. Now he's an Edinburgh cop who hides from his memories, misses promotions and ignores a series of crank letters."

book1 = Book("Empire of Black and Gold", "Adrian Tchaikovsky", "Fantasy", desc1, True)
book2 = Book("Leviathan Wakes", "James S. A. Corey", "Science Fiction", desc2, False)
book3 = Book("Knots and Crosses", "Ian Rankin", "Crime", desc3 , True)

books = [book1, book2, book3]


def add_new_book(book):
    books.append(book)

def delete_book(index):
    books.pop(index)