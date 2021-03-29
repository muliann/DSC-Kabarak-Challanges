
"""
Mad Lab Generator
Create your own Mad Libs generator that a user can interact with. 
It will help you understand concepts like strings, variables, and concatenation. 
Mad Libs Generator teaches to manipulate user-inputted data as the Mad Libs refer to a series of inputs that a user enters.
 The input from the user could be anything from an adjective, a pronoun, or even a verb.
  After all the inputs are entered the application takes all the data and arranges it to build a story template. """
adj=input("adjective:") #beautiful
adj_2=input("adjective:") #better
conjuction=input("conjuction:") #than
verb=input("verb:") #nested
print("\n")
print("The Zen of Python")
print(adj +" is better than ugly")
print("Explicit is better than implicit.")
print("Simple is " +adj_2+ " than complex.")
print("Complex is better "+conjuction+" complicated.")
print("Flat is better than "+verb)


