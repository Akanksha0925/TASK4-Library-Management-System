Rollnum = ["20BF1A1201","20BF1A1202","20BF1A1203","20BF1A1204","20BF1A1205","20BF1A1206","20BF1A1207","20BF1A1208","20BF1A1209","20BF1A1210","20BF1A1211","20BF1A1212","20BF1A1213","20BF1A1214","20BF1A1215","20BF1A1216","20BF1A1217","20BF1A1218","20BF1A1219","20BF1A1220","20BF1A1221","20BF1A1222","20BF1A1223","20BF1A1224","20BF1A1225","20BF1A1226","20BF1A1227","20BF1A1228","20BF1A1229","20BF1A1230"]
username = input("Enter your Id")
if username in Rollnum:
    class library:

        def __init__(self, booklist):
            self.books = booklist

        def AvailableBooks(self):
            print("\nBooks in the library are: \n")
            for book in self.books:
                print(">"+book)

        def BorrowBook(self, BookName):
            if BookName in self.books:
                print(
                    f"Your required book named {BookName} is issued.\nEnjoy reading book and return it before 30 days")
                self.books.remove(BookName)
            else:
                print(
                    f"Sorry\nYour requsted book named {BookName} is not available in the Library.\nPlease wait until the book is available.")

        def ReturnBook(self, BookName):
            self.books.append(BookName)
            print("Hope you enjoyed the book")

        def Donate(self, Bookname):
            self.books.append(Bookname)
            print("Thank you so much for donating books to our library.\n Have a great day ")

        def KnowAboutBook(Bookname):
            if Bookname == "Clean Code: By Robert C. Martin":
                print("This is one of the best classic books for beginners and will teach you all tricks and patterns of writing good and clean code. Every code which runs is not a clean code. Most of the beginner programmer done this mistake, they just try to solve the problem and hence forgets these factors to write a clean and perfect professional code. A Clean Code should be properly readable, well structured so that it could be reused and debug easily. \
                \
                Ideas Presented:\
                    \
                    How to properly name a variable?\
                    How to write a better method?\
                    How to structure your code better?\
                    What is the code smell?\
                    Why another approach is better than this one?")
            elif Bookname == "The Mythical Man-month: By Frederick Brooks":
                print("According to many software developers in the world, this book is literally a Bible to them. This book will help you build a proper concept about software development, estimates, project management, and troubles in software development. The main theme of this book is “Brooks Law ” which says “adding manpower to a late software project makes it later”. \
                    \
                Ideas Presented:\
                    \
                        The mythical man-month: measuring useful work in man-months is a myth,\
                        Essence and Accidents of Software Engineering,\
                        When working on a second system, you should keep in mind that you shouldn’t over-engineer it,\
                        Any attempt to fix a errors can lead you to many new errors.\
    ")
            elif Bookname == "The Pragmatic Programmer: Your Journey to Mastery":
                print("This is book is Andrew Hunt and David Thomas, about programming and software engineering. The unique feature of this book is it teaches us in a pragmatic way with a collection of tips to improve the programming and development process rather than the theoretical way. This book will help you to become a pragmatic programmer, an early adopter, to have fast adaptation, inquisitiveness and critical thinking, realism, and being a jack-of-all-trades. The book presents development methodologies and caveats, analogies and short stories too, for example, the broken windows theory, the story of the stone soup, or the boiling frog.\
                    \
                Ideas presented:\
                    \
                Present development methodologies and process using many analogies and short stories. e.g, the stone soup, or the story of the boiling frog\
                Many concepts were named which get popular for this book, such as code katas,\
                More use of methods for making and preserving codes highly adjustable,\
                Useful recommendations for estimates of time and expense\
                Introduces you to methods of work that you may not yet have considered.")
            elif Bookname == "Code Complete (2 Edition): By Steve McConnell":
                print("If you are want to be a great software engineer you should read this book once. This book provides the most useful practical guides of programming and helping developers write better software for more than a decade. This book has the rare blend of classic and fully updated with revised leading-edge coding concepts and example. With these proper concepts, you can easily understand the art and science of software construction. \
                    \
                Ideas Represented: \
                        \
                Software craftsmanship, e.g, layout, style, character, themes and self-documentation\
                Coding, debugging, integration and testing for software development,\
                Other important software development aspects such as requirements and documentation,\
                The techniques of creating a high-quality code, code improvements and system considerations.")
            elif Bookname == "The Art of Computer Programming":
                print("This is another classic book written by the famous computer scientist Professor Donald Knuth. This book is very popular and highly praised by many of the top programmers in the world for the combined mathematical exactness with an outstanding humour throughout the chapters.  Through his well-known book series ‘art of computer programming’, for his major contributions to the analysis of algorithms, Knuth was awarded the Turing Award in 1974. \
                The book begins with basic programming concepts and techniques, explores various programming algorithms and describes their analysis efficiently and then focuses particularly on the representation of information inside a computer(information structure). \
                \
                \
                Ideas Presented:\
                \
                _> How to deal with the structural relationships between data elements efficiently,\
                    > How to solve problems effectively using the basic concepts of fundamental Algorithms,\
                    > Semi-numerical Algorithms and Combinatorial Algorithms\
                    > Minimum-Comparison Sorting or Optimum Sorting")
            elif Bookname == "Programming Pearls":
                print("This book is slightly different from the other classics books on the list but this book is one of the most influential books to helps a person think like a programmer. Every concept is properly covered with practical problems and various effective and efficient solutions. This is pleasant to read because the writing style is simply great. \
                    \
                This book may not a usual book of new programming concepts but it is the best practical programming book to practice and follow with clear cut examples. The book challenges your understanding of the core concepts in memory, CPU, and algorithms and gradually increment the difficulties rather than giving you the answer right away because the main motto of this book is to help you become a better problem solver. This book is the best place to practice problems of data structure and algorithms especially searching, sorting, heaps etc. It Is really a masterpiece created by Jon Bentley fully justifying the name “Programming Pearls”. ")
            
            elif Bookname == "Code: Charles Petzold":
                print("This book introduces us with “The Hidden Language of Computer Hardware and Software” in an outstanding way for anyone who’s ever wondered about the magic and secret inner life of computers and how the working of these complex system and other smart machines.\
                \
                Nowadays the low-level details gets masked due to the level of abstractions but if you go through this book you can understand those awesome older technologies like Morse code, Braille, and Boolean logic, to understand vacuum tubes, transistors, and integrated circuits. Sometimes to solve a very complicated bug you have to drive deeper to the dead ends of the electronic, binary computer with a von Neumann architecture to reach a scalable solution. It also easily explained many recent developments topics, like floating-point arithmetic, operating systems, packet-based communication protocols, and GUIs. ")
            elif Bookname == "Introduction to Algorithms":
                print("This is the single famous book widely used as the textbook for understanding and using an algorithm by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. With over 10, 000 citations documented on CiteSeerX, this book is commonly cited as a reference for algorithms in published papers. The book was also a bestseller programming book with half a million sold copies during its first 20 years.\
                    \
                Each chapter in this book covers a broad range of algorithms, its design techniques and areas of application in depth. Instead of a specific programming language, programming examples are written using pseudo code with rigor and comprehensiveness. ")
            elif Bookname == "Refactoring: Improving the Design of Existing Code":
                print("This book is written by y Martin Fowler is an essential book for software developers which offers start-to-finish strategies for working more effectively with large software and improving the design of existing code.\
                    \
                Refactoring is the process of rewriting codes, without changing the functionality, to improve the readability, testability, or maintainability of your code. If you are interested in improving and maintaining the quality of your code this book is for you which contains step by step instructions for implementation of more than 40 proven refactorings example illustrating with details as to when and why to use the refactoring. In the second edition of this classic book, it switched from Java to JavaScript for most of the examples but the ideas can be applied to any Object-oriented programming language. The book is well written, provides samples, examples, diagrams, steps to follow, side-notes, commentary, and basically everything you would need to fully understand a refactoring method.")
            elif Bookname == "Design Patterns: Elements of Reusable Object-Oriented Software":
                print("This is hailed as one of the greatest software development books ever written\
                    describing into great detail on the many different design patterns. It has been influential to the field of software engineering and was written by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, with a foreword by Grady Booch.\
                    \
                    This book is a must-read for a budding architect or designer of a complex system. You will most likely be required to read this book to avoid and handle common problems that the industry faces. This book contains the in -detail description of the many different design patterns and regarded as an important source for object-oriented design theory and practice that have been developed over the years to help software engineers.\
                        \
                    The authors discuss various things like the tension between inheritance and encapsulation, parameterized types, Supporting Multiple Look-And-Feel Standards, Embellishing the User Interface, Supporting Multiple Window Systems etc.")
            else:
                print("Sorry,Your Requested book description not availabe.")


    class Student:
        def RequestBook(self):
            self.book = input("Enter the book name you want to borrow:\t")
            if self.book == " ":
                print("enter valid name")
            else:
                return self.book

        def ReturnBook(self):
            self.book = input("enter the book name you want return it:")
            if self.book == " ":
                print("enter valid name")
            else:
                return self.book


    if __name__ == "__main__":
        CenLib = library(["Clean Code: By Robert C. Martin", "The Mythical Man-month: By Frederick Brooks", "The Pragmatic Programmer: Your Journey to Mastery", "Code Complete (2 Edition): By Steve McConnell", "The Art of Computer Programming",
                        "Programming Pearls", "Code: Charles Petzold", "Introduction to Algorithms", "Refactoring: Improving the Design of Existing Code", "Design Patterns: Elements of Reusable Object-Oriented Software"])
        student = Student()
        while (True):
            print("\n\n\n******************** WELCOME TO CENTRALLIBRARY ********************\n\n\
                1> List of Books\n\
                2> Borrow Book\n\
                3> Return Book\n\
                4> Donate Book\n\
                5> Know About Book\n\
                6> Exit")
            a = int(input("\n\nEnter your Choice:"))
            if a == 1:
                CenLib.AvailableBooks()
            elif a == 2:
                CenLib.BorrowBook(student.RequestBook())
                print("Thanks for using our library. Keep reading ")
            elif a == 3:
                CenLib.ReturnBook(student.ReturnBook())
                print("Thanks For returning.\n Have a Good Day ")
            elif a == 4:
                CenLib.Donate(student.ReturnBook())
            elif a == 5:
                kab=input("Enter the book name that you want to know.")
                library.KnowAboutBook(kab)
           
            else:
                print("Invalid Choice \n Try Again")
    else:
        print("you have no access to use this Library Sorry")