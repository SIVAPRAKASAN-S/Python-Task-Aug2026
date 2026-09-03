# spliting and joining of string



# Splitting and Joining


# str.split(delimiter) – Splits string into list 
# str.rsplit(delimiter) – Splits from the right 
# str.splitlines() – Splits on newline characters
# str.join(iterable) – Joins elements using the string as a separator 
# str.format() – Inserts values into a string f"{}" – f-strings (Python 3.6+)



# str1="python programming"   
# result=str1.split()  # spliting of string
# print(result)


# csv_data = "apple,banana,cherry" 
# result = csv_data.split(",") 
# print(result) 

# text="    hello world  " 
# print(text.strip())

# text="$$$$$Python$$$"
# print(text.strip('$'))

# text="$$$$$Python$$$"
# print(text.lstrip('$'))

# text="$$$$$Python$$$" 
# print(text.rstrip('$'))

# text="   he  ll  o wo rl d "
# print(text.replace(" ",""))

# List of strings
# words = ["Hello", "world", "from", "Python"]
#  # Join the words with a space separator
# sentence = " ".join(words)