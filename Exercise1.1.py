#Exercise 1.1
sakheli = input("What is your name? ").title()
sakheli_da_gvari = sakheli.split()

sakheli_final = " ".join(sakheli_da_gvari)
print("Hello,", sakheli_final + ".", "Nice to meet you. How can I help you?" )
