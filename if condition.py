watch = input("watch is expensive than glasses?(y/n)").upper()
glasses = input("glasses are cheaper than watch?(y/n)").upper()

if watch == "Y":
    print("i like watches!")
if glasses == "Y":
    print("i like glasses!")

# PYTHON 3
# I DIDN'T UNDERSTAND YOUR CODE, SORRY, I'LL DO SOME MODIFICATIONS

watch = int(input("How much cost a watch? "))
glasses = int(input("How much cost glasses? "))

if glasses > watch:
    print("The watch is cheaper than the glasses")
if gasses < watch: # you can also use "else" statement here.
    print("The glasses are cheaper than the watch")
