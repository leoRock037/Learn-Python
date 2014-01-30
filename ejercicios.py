def ex1():
	
	#print "Hello World!"
	print "Hello Again!"
	print "I like typing this."
	print "This is fun."
	print 'Yay! printing.'
	print "I'd much rather you 'not'."
	print 'I "said" do not touch this.'

	print "Cristian"

def ex2():

	# A comment, this is so you can read your program later
	# Anything after the # is ignored by python
	print "I could have code like this" # and the comment after is ignored
	# You can also use a comment to "disable" or comment out a piece of code:
	# print "This won't run"
	print "this will run"
	
def ex3():
	print "I will now count my chickens: "
	print "Hens", 25+30/6
	print "Roosters", 100-25 *3 %4
	print "Now I will count the eggs:"
	print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
	print "Is it true that 3+2<5-7?"
	print 3+2<5-7
	print "What is 3 + 2 ? ", 3 + 2
	print "What is 5 - 7?", 5 - 7
	print "Oh, that's why it's False."
	print "How about some more."
	print "Is it greater?", 5 > -2
	print "Is it greater or equal?", 5 >= -2
	print "Is it less or equal?", 5 <= -2

def ex4():

	cars=100
	space_in_a_car=4.0
	drivers=30
	passengers=90
	cars_not_driven=cars - drivers
	cars_driven = drivers
	carpool_capacity =cars_driven * space_in_a_car
	average_passengers_per_car =passengers / cars_driven

	print "There are", cars ,"cars available."
	print "There are only ", drivers , "drivers  available"
	print "There will be ", cars_not_driven , "empty cars today."
	print "we can transport ", carpool_capacity,"people today. "
	print "we have ", passengers, "to carpool today."
	print "we need to put about ", average_passengers_per_car, "in each car."

def ex5():
	name = 'Zed A. Shaw'
	age = 35 # not a lie
	height = 74 # inches
	weight = 180 # lbs
	eyes = 'Blue'
	teeth = 'White'
	hair = 'Brown'

	print "Let's talk about %s."% name 
	print "He's %d inches tall." % height
	print "He's %d pounds heavy." % weight
	print "Actually that's not too heavy."
	print "He's got %s eyes and %s hair." % (eyes,hair)
	print "His teeth are usually %s depending on the coffee." % teeth

	# this line is tricky, try to get it exactly right
	print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
	print 'esto es una prueva%r, eyes %r ' % (name,eyes)

def ex6():

	x= "There are %d types of people. "% 10
	binary = "binary"
	do_not ="do_not"
	y = "Those who know %s and those who %s."%(binary, do_not)

	print x
	print y

	print "I said: %r" % x
	print "I also said: '%s'." %Y

	hilarious = False
	joke_evaluation = "Isn't that joke so funny?! %r"

	print joke_evaluation % hilarious

	w = "This is the left side of..."
	e = "a string with a right side."

	print w + e

def ex7():
	print "Mary had a little lamb."
	print "Its fleece was white as %s."% 'snow'
	print "And everywhere that mary went."
	print "."* 10 #what that do? ...multiplica el numero de puntos

	end1 = "C"
	end2 = "h"
	end3 = "e"
	end4 = "e"
	end5 = "s"
	end6 = "e"
	end7 = "b"
	end8 = "u"
	end9 = "r"
	end10 = "g"
	end11 = "e"
	end12 = "r"

	# watch that comma at the end.  try removing it to see what happens
	print end1 + end2 + end3 + end4 + end5 + end6, #removing the comma is an error
	print end7 + end8 + end9 + end10 + end11 + end12

def ex8():
	formatter = "%r %r %r %r"

	print formatter % (1,2,3,4)
	print formatter % ("one","two","three","four")
	print formatter % (True,False,True,False)
	print formatter % (formatter,formatter,formatter,formatter)
	print formatter % ("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight.")
	
def ex9():
	days = "Mon Tue Wed Thu Fid Sat Sun"
	months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

	print "here are days: ", days
	print "here are the months: %s" % months

	print """There's something going on here.
	With the three double-quotes.
	We'll be able to type as much as we like.
	Even 4 lines if we want, or 5, or 6.
	"""

def ex10():
	tabby_cat = "\tI'm tabbed in."
	persian_cat = "I'am split\nom a line"
	backslash_cat = "I'm \\ a \\ cat."
	
	fat_cat = """
	I'll do a list:
	\t* Cat food
	\t* Fishies
	\t* Catnip\n\t* Grass
	"""
	print tabby_cat
	print persian_cat
	print backslash_cat
	print fat_cat

def ex11():
	print "How old are you?",
	age = raw_input()
	print "How tall are you?",
	height = raw_input()
	print "How much do you weigh?",
	weight = raw_input()

	print "so, you're %r old,%r tall and %r heavy."%(age,height,weight)


def ex12():
	age = raw_input("How old are you?")
	height =raw_input("How tall are you?")
	weight= raw_input("How much do you weigh?")

	print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


def ex13():
	#NOTA: Para ejecutar Ejercicios con argumentos pasarselos al momento de ejecutar el archivo ,
	#Ejmplo: python ejercicios.py first second third
	from sys import argv
	script, first, second, third = argv
	print "The script is called:",script
	print "Your first variable is:",first
	print "Your second variable is:",second
	print "Your third variable is:",third	

def ex14():
	
	from sys import argv

	script, user_name = argv
	prompt = '> '

	print "Hi %s, I'm the %s script." % (user_name, script)
	print "I'd like to ask you a few questions."
	print "Do you like me %s?" % user_name
	likes = raw_input(prompt)

	print "Where do you live %s?" % user_name
	lives = raw_input(prompt)

	print "What kind of computer do you have?"
	computer = raw_input(prompt)

	print """
	Alright, so you said %r about liking me.
	You live in %r.  Not sure where that is.
	And you have a %r computer.  Nice.
	""" % (likes, lives, computer)

def ex15():
	#Nota: Necesario crear archivo .txt e indicar en los args
	from sys import argv
	script , filename =argv
	txt =open(filename)

	print "Here's your file %r: "% filename
	print txt.read()

	print "Type the filename again:"
	file_again =raw_input("> ")

	txt_again = open (file_again)
	print txt_again.read()

def ex16():

	from sys import argv

	script, filename = argv

	print "We're going to erase %r." % filename
	print "If you don't want that, hit CTRL-C (^C)."
	print "If you do want that, hit RETURN."
	raw_input("?")
	print "Opening the file..."
	target = open(filename, 'w')
	print "Truncating the file.  Goodbye!"
	target.truncate()
	print "Now I'm going to ask you for three lines."

	line1 = raw_input("line 1: ")
	line2 = raw_input("line 2: ")
	line3 = raw_input("line 3: ")

	print "I'm going to write these to the file."
	target.write(line1)
	target.write("\n")
	target.write(line2)
	target.write("\n")
	target.write(line3)
	target.write("\n")

	print "And finally, we close it."
	target.close()

def ex17():

	from sys import argv
	from os.path import exists

	script, from_file , to_file =argv
	print "Copying form %s to %s " % (from_file, to_file)

	# we could do these two on one line too, how?
	in_file = open(from_file)
	indata = in_file.read()

	print "The input file is %d bytes long"%len(indata)
	print "Does the output file exist? %r " %exists(to_file)
	print "Ready, hit RETURN to continue, CTRL-C to abortt."

	raw_input()

	out_file =open(to_file, 'w')
	out_file.write(indata)

	print "Alright, all done."

	out_file.close()
	in_file.close()

def ex18():

	# this one is like your scripts with argv
	def print_two(*args):
	    arg1, arg2 = args
	    print "arg1: %r, arg2: %r" % (arg1, arg2)

	# ok, that *args is actually pointless, we can just do this
	def print_two_again(arg1, arg2):
	    print "arg1: %r, arg2: %r" % (arg1, arg2)

	# this just takes one argument
	def print_one(arg1):
	    print "arg1: %r" % arg1

	# this one takes no arguments
	def print_none():
	    print "I got nothin'."


	print_two("Zed","Shaw")
	print_two_again("Zed","Shaw")
	print_one("First!")
	print_none()


def ex19():

	def cheese_and_crackers(cheese_count,boxes_of_crackers):
		print "You have %d cheeses!" % cheese_count
		print "You have %d boxes of crackers!" % boxes_of_crackers
		print "Man that's enough for a party!"
		print "Get a blanket.\n"

	print "We can just give the function numbers directly:"
	cheese_and_crackers(20, 30)

	print "OR, we can use variables from our script:"
	amount_of_cheese = 10
	amount_of_crackers = 50

	cheese_and_crackers(amount_of_cheese, amount_of_crackers)

	print "we can even do math inside too:"
	cheese_and_crackers(10 + 20, 5 + 6)
	print "And we can combine the two, variables and math:"
	cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def ex20():#necesita argv para ser ejecutado
	
	from sys import argv
	script, input_file = argv

	def print_all(f):
	    print f.read()

	def rewind(f):
	    f.seek(0)

	def print_a_line(line_count, f):
	    print line_count, f.readline()

	current_file = open(input_file)
	print "First let's print the whole file:\n"
	print_all(current_file)
	print "Now let's rewind, kind of like a tape."
	rewind(current_file)
	print "Let's print three lines:"

	current_line = 1
	print_a_line(current_line, current_file)

	current_line = current_line + 1
	print_a_line(current_line, current_file)

	current_line = current_line + 1
	print_a_line(current_line, current_file)

def ex21():

	def add(a,b):
		print "ADDING %d + %d"%(a,b)
		return a + b
	def subtract(a,b):
		print "SUBTRACTING %d-%d"%(a,b)
		return a-b
	def multiply(a,b):
		print "MULTIPLYING %d*%d"%(a,b)
		return a*b
	def divide(a,b):
		print "DIVIDING %d/%d "%(a,b)
		return a/b

	print "Lest's do some math with just functions!" 

	age = add(30,5)
	height=subtract(78,4)
	weight=multiply(90,2)
	iq=divide(100,2)

	print age
	print height
	print weight
	print iq


	print "age:%d, height:%d, weight: %d, Iq: %d"%(age,height,weight,iq)

	print "Here is a puzzle."
	what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
	print "That becomes: ", what, "Can you do it by hand?"

def ex24():
	print "Let's practice everything."
	print 'You\'d need to know \'bout escapes with\\ that do \n newlines and \t tabs.'

	poem = """
	\tThe lovely world
	with logic so firmly planted
	cannot discern \n the needs of love
	nor comprehend passion from intuition
	and requires an explanation
	\n\t\twhere there is none.
	"""

	print "--------------"
	print poem
	print "--------------"


	five = 10 - 2 + 3 - 6
	print "This should be five: %s" % five

	def secret_formula(started):
	    jelly_beans = started * 500
	    jars = jelly_beans / 1000
	    crates = jars / 100
	    return jelly_beans, jars, crates


	start_point = 10000
	beans, jars, crates = secret_formula(start_point)

	print "With a starting point of: %d" % start_point
	print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

	start_point = start_point / 10

	print "We can also do that this way:"
	print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


def ex29():

	people = 20
	cats = 30
	dogs = 15
	if people < cats:
	    print "Too many cats! The world is doomed!"
	if people > cats:
	    print "Not many cats! The world is saved!"
	if people < dogs:
	    print "The world is drooled on!"
	if people > dogs:
	    print "The world is dry!"
	dogs += 5

	if people >= dogs:
	    print "People are greater than or equal to dogs."
	if people <= dogs:
	    print "People are less than or equal to dogs."
	if people == dogs:
	    print "People are dogs."

def ex30():

	people = 30
	cars = 40
	buses = 15


	if cars > people:
	    print "We should take the cars."
	elif cars < people:
	    print "We should not take the cars."
	else:
	    print "We can't decide."

	if buses > cars:
	    print "That's too many buses."
	elif buses < cars:
	    print "Maybe we could take the buses."
	else:
	    print "We still can't decide."

	if people > buses:
	    print "Alright, let's just take the buses."
	else:
	    print "Fine, let's stay home then."

def ex31():

	print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"
	door = raw_input("> ")

	if door == "1":

	    print "There's a giant bear here eating a cheese cake.  What do you do?"
	    print "1. Take the cake."
	    print "2. Scream at the bear."

	    bear = raw_input("> ")

	    if bear=="1":
	        print "The bear eats your face off.Good job!"
	    elif bear=="2":
	        print "The bear eats your legs off.Good job!"
	    else:
	        print "Well, doing %s is probably better.Bear runs away."%bear

	elif door == "2":
	    print "You stare into the endless abyss at Cthulhu's retina."
	    print "1. Blueberries."
	    print "2. Yellow jacket clothespins."
	    print "3. Understanding revolvers yelling melodies."

	    insanity = raw_input("> ")

	    if insanity == "1" or insanity == "2":
	        print "Your body survives powered by a mind of jello.Good job!"
	    else:
	        print "The insanity rots your eyes into a pool of muck.Good job!"

	else:
	    print"You stumble around and fall on a knife and die.Good job!"

def ex32():

	the_count=[1,2,3,4,5]
	fruits =['apples','oranges','pears','apricots']
	change =[1,'pennies',2,'dimes',3,'quarters']

	# this first kind of for-loop goes through a list

	for number in the_count:
		print "This is count %d"%number

	#save as above

	for fruit in fruits:
		print "A fruit of type %s"%fruit

	for i in change:
		print "I got %r"%i

	elements = []

	#the use the range function to do 0 to 5
	for i in range(0,6):
		print "Adding %d to the list" % i
		#append is a function that list understand
		elements.append(i)

	for i in elements:
		print "Element was: %d"%i

def ex33():
	
	i=0
	numbers=[]

	while i<6:
		print "At the top i is %d"%i
		numbers.append(i)

		i=i+1
		print "Numbers now: ",numbers
		print "At the bottom i is %d" %i

	print "the numbers: "

	for num in numbers:
		print num

def ex34():

	animals = ['bear','python','peacock','kangaroo','whale','platypus']

	print "The animal at 1: %s" % animals[1]
	print "The third (3rd) animal: %s" % animals[2]
	print "The first (1st) animal: %s" % animals[0]
	print "The animal at 3: %s" % animals[3]
	print "The fifth (5th) animal: %s" % animals[4]
	print "The animal at 2: %s" % animals[2]
	print "The sixth (6th) animal: %s" % animals[5]
	print "The animal at 4: %s" % animals[4]



ex={'1':ex1,'2': ex2,'3': ex3,'4':ex4,'5': ex5,'6':ex6, '7':ex7,'8':ex8,'9':ex9,'10':ex10,
'11':ex11,'12':ex12,'13':ex13,'14':ex14,'15':ex15,'16':ex16,'17':ex17,'18':ex18,'19':ex19,
'20':ex20,'21':ex21,'29':ex29,'30':ex30,'31':ex31,'32':ex32,'33':ex33,'34':ex34}

opcion=raw_input('elija un ejercicio del numero 1 al 34 :  ')
try:
	op=ex[opcion]()
except:
	print 'Escoja un ejercicio valido'