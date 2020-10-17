# list = [".....", "...","........."]           /remove /add /slicing [0:len:1]
# tuple = ("....", " ... ", ".")               /can not delete any value once intialise
# dictionary = { "...":"... , ....", "....." : { "...":"....."}}
# set = ([1,2,4,5,6]) it stores the unique value only
# set = (list)              /union  /intersection /len /min /max /difference /isdisjoint /remove /add
# input() for getting input (string always)
# print() for showing output
# if 3 not in list : ...               elif 4 in list: ......    else : .....             indentation is necessary
# for x in list: .......
# while x>4: ........
# ** used to power an operator like 5**3 = 125
# function  |.builtin  name(list or tuple (iteration))   |.userdefine  a keyword is used "def"  def fuctionname():
# doc string is used to know the use of userdefine fucntion.  comment in the first line ,   ficntionname.__doc__
# try: ........  except exception as e: print(e)              //trycatch in java is tryexcept here

"""
file operations

"w" write mode
"r" read mode    (default mode)
"a" append mode i.e add more content to the end of the file
"+" both read and write mode
"b" binary mode , for dealing with binary files only
"t" text mode, for dealing with text file only         (default mode)
"x" create a file if not exists

f=open("file name","a"#mode)   //saving file pointer in f for further operations
for print lines without reading say |for line in f:|
for reading of a single line write |f.readline()|
for converting files lines into list use |f.readlines()|

f.seek(position like 0 )  to move pointer to a specific position
f.tell() tells you the current pointer position

we can also open the file like this and in this we haven,t need to clos the file
|with saggy.txt as f:|

"""

# args - used in the function    | deg funcname(*argssagar):|
# and calling |functionname(*list or tuple)|         its type is tuple and it is used when our list is changing
# normal then args and then kwargs.
# kwargs -  double star ** (dictionary takes)

# fstring are used to add other string in between or doing any calculation in the "...."
# f" {key} is a father of {value}" where key and value are other strings

"""
time module
import time
-time.time()  gives to current clock tic just like stop watch
-local time = time.asctime(time.localtime(time.time()))
- time.sleep(2)    this will delay the execution by 2 second   *vimp 
"""

# join function will let you add any string in between the list items

# map funtion will let you operate any other function into the lst item
# it returns the object thats why we type cast map into list further

# similarly filter will let you enter boolean funtion into list item for true response
# and reduce function will let you reduce the list item by operating on the function

