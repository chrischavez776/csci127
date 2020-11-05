#Name: Christian Chavez
#Email: christian.chavez01@myhunter.cuny.edu
#Date: 11/05/2020
#This program computes LIRR fare

def computeFare(zone, ticketType):
    fare = 0
    if (zone == 1) and (ticketType == 'peak'):
        fare = 8.75
    elif (zone == 1) and (ticketType == 'off-peak'):
        fare = 6.75
    elif (zone == 2) and (ticketType == 'peak'):
        fare = 10.25
    elif (zone == 2) and (ticketType == 'off-peak'):
        fare = 7.50
    elif (zone == 3) and (ticketType == 'peak'):
        fare = 10.25
    elif (zone == 3) and (ticketType == 'off-peak'):
        fare = 7.50
    elif (zone == 4) and (ticketType == 'peak'):
        fare = 12.00
    elif (zone == 4) and (ticketType == 'off-peak'):
        fare = 8.75
    elif (zone == 5) and (ticketType == 'peak'):
        fare = 13.50
    elif (zone == 5) and (ticketType == 'off-peak'):
        fare = 9.75
    elif (zone == 6) and (ticketType == 'peak'):
        fare =13.50
    elif (zone == 6) and (ticketType == 'off-peak'):
        fare = 9.75
    elif (zone == 7) and (ticketType == 'peak'):
        fare = 13.50
    elif (zone == 7) and (ticketType == 'off-peak'):
        fare = 9.75
    else:
        fare = -5
    return(fare)

def main():
  z = input('Enter the number of zones: ')
  t = input('Enter the ticket type(peak/off-peak): ').lower()
  fare = computeFare(z,t)
  print('The fare is', fare)

if __name__ == "__main__":
  main()
