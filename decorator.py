#CLOSURE OF A FUNCTION

print("======CLOSURE===========")

def outer_function():
	message = "This is a msg"
	def inner_function():
		print(message)
	return inner_function()
	
outer_function()

print("=================")

def outer_function():
	message = "This is a msg"
	def inner_function():
		print(message)
	return inner_function
	
display_func = outer_function()
display_func()

print("=================")

def outer_function(argument):
	def inner_function():
		print(argument)
	return inner_function
	
display_func_hi = outer_function("Hi, this is argument")
display_func_hi()


print("=========DECORATOR========")

def decorator_function(original_function):
	def wrapper_function():
		print("wrapper function executed")
		return original_function()
	return wrapper_function()

def display_func():
	print("Display function executed")
	
decorator_function(display_func)

print("=================")

def decorator_function(original_function):
	def wrapper_function():
		print("wrapper function executed")
		return original_function()
	return wrapper_function
	
def display_func():
	print("The nile song")
	
call_decorator = decorator_function(display_func)
call_decorator()

print("=================")

def decorator_function(original_function):
	def wrapper_function():
		print("Wrapper function executed")
		return original_function()
	return wrapper_function
	
@decorator_function
def display():
	print("Let there be more light")
	
display()

print("========Positional argument decorator function=========")

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print("Wrapper function executed")
		return original_function(*args, **kwargs)
	return wrapper_function
	
@decorator_function
def display_info(name, age):
	print("name {}, age {}".format(name,age))
	
display_info("John", 25)

@decorator_function
def display_text():
	print("This text is displayed")
	
display_text()

print("========Class decorator=========")

class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function
		
	def __call__(self, *args, **kwargs):
		print("Call method executed")
		return self.original_function(*args,**kwargs)
		
@decorator_class
def display_text():
	print("Text displayed")
	
@decorator_class
def display_info(name,age):
	print('my name is {}, {} yo'.format(name,age))
	
display_text()
display_info('Jack', 16)