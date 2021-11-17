from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bids = {}
bol = True
print("Welcome to the secret auction program")
while bol:
  name = input("What is your name? ")
  bid = int(input("Whats your bid? "))
  bids[name] = bid
  more_bids = input("Are there any other bidders? Type yes or no: ")
  if more_bids == "yes":
    clear()
  elif more_bids == "no":
    bol = False
    max_bid = 0
    winner = ''
    for b in bids:
      if bids[b] > max_bid:
        max_bid = bids[b]
        winner = b
    print(f"The winning bid is {max_bid}, made by {winner}")

