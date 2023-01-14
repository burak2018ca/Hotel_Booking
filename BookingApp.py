#-------------------------------------------------------------------------------------------------#
#   Imports                                                                                       #
#-------------------------------------------------------------------------------------------------#
import datetime, calendar, sys, openpyxl
from calendar import monthrange


#-------------------------------------------------------------------------------------------------#
#   Global Fields                                                                                 #
#-------------------------------------------------------------------------------------------------#

gv_Hotels = []

gv_Booked_Hotels = []

class Hotel:
    def __init__(self):
        self.name = ""
        self.city = ""
        self.country = ""
        self.starrate = 0 
        self.price = 0
    def reset(self):
        self.name = ""
        self.city = ""
        self.country = ""
        self.starrate = 0
        self.price = 0

class Reservation:
    def __init__(self):
        self.year = 0 
        self.month = 0
        self.day = 0 
        self.nights = 0 
        self.cost = 0
        self.dayname = ""
        self.roomtype = ""
    def reset(self):
        self.year = 0
        self.month = 0
        self.day = 0 
        self.nights = 0
        self.cost = 0
        self.dayname = ""
        self.roomtype = ""


new_hotel = Hotel()
new_reservation = Reservation()

#-------------------------------------------------------------------------------------------------#
#   Main Function                                                                                 #
#-------------------------------------------------------------------------------------------------#

def main():

    Load_Data_From_Excel()

    User_Input = ""

    while User_Input != "6":

        new_hotel.reset()
        new_reservation.reset()
       
        Print_Main_Menu()

        User_Input = input("\nEnter the number: ")

        if  (User_Input == "1"): menu_item1()
        elif(User_Input == "2"): menu_item2()
        elif(User_Input == "3"): menu_item3()
        elif(User_Input == "4"): menu_item4()
        elif(User_Input == "5"): menu_item5()
       
#-------------------------------------------------------------------------------------------------#
#   Menu Item 1 : Hotel Filter                                                                    #
#-------------------------------------------------------------------------------------------------#

def menu_item1():

    User_Input = ""
    while User_Input.lower() != "q": 
        hotel_filter()

        print("\n#---------------------------#")
        print("# (R) For Retry  (Q) For Quit #")
        print("#-----------------------------#")
        User_Input = input("\n")

def hotel_filter():
    Filter_Options = []
    Filtered_Hotels = []

    # Instructions
    print("""\nYou can filter hotels by their City and country they are placed.
 What is their star rating and lastly how much does it cost for one night stay""")

    # Getting Criterias from user
    Country = str(input("\nEnter the country name "))
    Filter_Options.append(f"COUNTRY: {Country}")

    City = str(input("\nEnter the city name "))
    Filter_Options.append(f"CITY: {City}")

    Star_Rate = int(input("\nPlease enter the star rating "))
    Filter_Options.append(f"STAR RATE: {Star_Rate}")

    Min_Cost = int(input("\nPlesae enter the expected minimum cost "))
    Filter_Options.append(f"MINIMUM COST: {Min_Cost}")

    Max_Cost = int(input("\nPlease enter the expected maximum cost "))
    Filter_Options.append(f"MAXIMUM COST: {Max_Cost}")

    # Printing Criterias
    print('\n\nHere is your criterias\n')
    for x in Filter_Options: print(f"{x}")

    # Funtion --> Filters the array by given criterias
    for x in range(0, len(gv_Hotels)):
        if (gv_Hotels[x][1].lower() == City.lower()  and  
            gv_Hotels[x][2].lower() == Country.lower() and  
            gv_Hotels[x][3] == Star_Rate  and
            gv_Hotels[x][4] >= Min_Cost and
            gv_Hotels[x][4] <= Max_Cost 
            ) : 
            Filtered_Hotels.append(gv_Hotels[x][0])

    if (len(Filtered_Hotels) == 0): Filtered_Hotels.append("NOT FOUND")
    # Printing the Hotels matches with criterias
    else: 
        print(f"\nhere is the hotels that matches with your criterias\n")
        List_num = 1
        for x in Filtered_Hotels:
            print(f"{List_num}. {x}")
            List_num += 1
 
#-------------------------------------------------------------------------------------------------#
#   Menu Item 2 : Hotel Search                                                                    #
#-------------------------------------------------------------------------------------------------#

def menu_item2():
    User_Input = ""
    while User_Input.lower() != "q": 
        hotel_search()

        print("\n#---------------------------#")
        print("# (R) For Retry  (Q) For Quit #")
        print("#-----------------------------#")      
        User_Input = input("\n")

def hotel_search():
    # Instructions
    print("\nType the name of the hotel and it will give you the features of that hotel")

    # User Input
    User_int = str.upper(input(""))
    found = False
    for x in range(0, len(gv_Hotels)):
        Selected_hotel = str.upper(gv_Hotels[x][0])
        print(f"{x}) " + Selected_hotel)
        if (Selected_hotel == User_int):
            found = True
            print(f"\n\n\n  {User_int}")
            print("-" * (len(User_int) + 4))
            print(f" Hotel is in the {gv_Hotels[x][2]}")
            print(f"\n Hotel is placed in the city of {gv_Hotels[x][1]}")
            print(f"\n Hotel has a {gv_Hotels[x][3]} star quality")
            print(f"\n Cost of one night stay is ${gv_Hotels[x][4]}")

    if(found == False):
        print("\n"+User_int)
        print(Selected_hotel)  
        print(len(gv_Hotels))
        print(f"{x}) couldn't find the hotel you are looking for\n")
                

#-------------------------------------------------------------------------------------------------#
#   Menu Item 3 : Booking Hotel                                                                   #
#-------------------------------------------------------------------------------------------------#

def menu_item3(): 
    User_Input = ""
    while User_Input.lower() != "q":

        print("\n\nWelcome, \nYou can find best prizes in hotels with our application. \nBe sure when you are booking do not enter a past date ")

        get_hotel_name()
        get_booking_date()
        price_calculations()
        print_information()

        print("\n#---------------------------#")
        print("# (R) For Retry  (Q) For Quit #")
        print("#-----------------------------#") 
        User_Input = input("\n")

def get_hotel_name():
    new_hotel.name = input("\n\nPlease enter the name of the Hotel\n")
    while not check_hotels_name(new_hotel.name):
        new_hotel.name = input("\n\nSorry we couldn't find what you are looking for \nPlease try again :)\n")

def get_todays_date():
    Current_Time = datetime.datetime.now()
    Current_Year = int(Current_Time.strftime("%Y"))
    Current_Month = int(Current_Time.strftime("%m"))
    Current_Day = int(Current_Time.strftime("%d"))
    return Current_Year, Current_Month, Current_Day

def check_hotels_name(name):
    for x in range(0, len(gv_Hotels)):
        if(gv_Hotels[x][0].lower() == name.lower()):
            return True,
    return False

def get_booking_date():
        
        Current_Year, Current_Month, Current_Day= get_todays_date()

        # ----- Get Year -----#
        new_reservation.year = int(input(
            f"\n\nPlease enter the year\nNote (Furthest date you can book is {Current_Year + 2})\n\n"))
        while(new_reservation.year < Current_Year or (Current_Year + 2) < new_reservation.year):  
            new_reservation.year = int(input("You entered invalid year choice\nPlease try again "))

        # ---- Get Month -----#
        print("\n\nJanuary = 1 \nFebruary = 2 \nMarch = 3 \nApril = 4 \nMay = 5 \nJune = 6 \nJuly = 7 \nAugust = 8 \nSeptember = 9 \nOctober = 10 \nNovember = 11 \nDecember = 12")
        new_reservation.month = int(input("Please enter the number of the month"))
        if(new_reservation.year == Current_Year):
            while(new_reservation.month > 12 or new_reservation.month < Current_Month):
                new_reservation.month = int(
                    input("\nYou entered invalid month choice\nPlease try again  "))
        elif(new_reservation.year > Current_Year):
            while(new_reservation.month > 12 or new_reservation.month < 0):
                new_reservation.month = int(
                    input("\nYou entered invalid month choice\nPlease try again  "))

        # ---- Get Day -----#
        Days_in_Month = monthrange(new_reservation.year, new_reservation.month)[1]
        print(f"\n{calendar.month_name[new_reservation.month]} has {Days_in_Month} days in it")
        new_reservation.day = int(input("Which day do you want to book your room "))

        if(new_reservation.year == Current_Year and new_reservation.month == Current_Month):
            while(new_reservation.day > Days_in_Month or new_reservation.day <= Current_Day):
                new_reservation.day = int(input("\nInvalid entry please try again\n"))
        else:    
            while(new_reservation.day > Days_in_Month or new_reservation.day < 0):
                new_reservation.day = int(input("\nInvalid entry please try again\n"))

        new_reservation.dayname = datetime.datetime(new_reservation.year, new_reservation.month, new_reservation.day)
        new_reservation.dayname = new_reservation.dayname.strftime("%A")
       
def price_calculations():
  
    Roomprice = 0 
    for x in range(0, len(gv_Hotels)):
       
        Hotelname = gv_Hotels[x][0]
        Hotelstar = gv_Hotels[x][3]
        Hotelprice = gv_Hotels[x][4]

        if(Hotelstar > 3 and new_hotel.name.lower() == Hotelname.lower()):
            print(f"""\n\nPlease select your room type\n
    1) Regular Suit = ${Hotelprice}
    2) Bussiness Suit = ${Hotelprice + 300}
    3) King Suit = ${Hotelprice + 1000}""")

            Room_Selection = int(
                input("\nPlease select the Suit type you want\n"))
            while(Room_Selection < 0 or Room_Selection > 3):
                Room_Selection = int(input("Invalid option, Please try again\n"))

            if(Room_Selection == 1):
                new_reservation.roomtype = "Regular Suit"
                Roomprice = Hotelprice

            elif(Room_Selection == 2):
                new_reservation.roomtype = "Bussiness Suit"
                Roomprice = Hotelprice + 300

            elif(Room_Selection == 3):
                new_reservation.roomtype = "King Suit"
                Roomprice = Hotelprice + 1000
        elif(Hotelstar <= 3 and new_hotel.name.lower() == Hotelname.lower()):
            print(f"\n\nRoom's price is ${Hotelprice}")
            Roomprice = Hotelprice
   
    Booked_Days = int(input("\n\nHow many nights will you be staying at the hotel\n"))

    new_reservation.cost = Roomprice * Booked_Days

def print_information():
    print("Here is your booking receipt\n")
    print(" ")
    print(f"Hotel Name: \n{new_hotel.name.upper()}")
    print(f"\nBooked Date: \n{new_reservation.day}/{new_reservation.month}/{new_reservation.year}  {new_reservation.dayname} 11:00 am")
    print(f"\nTotal Cost: \n$", format(new_reservation.cost,".2f"))

    Reservation = [new_hotel.name, new_reservation.day, new_reservation.month, new_reservation.year, new_reservation.dayname, new_reservation.roomtype, new_reservation.cost]
    gv_Booked_Hotels.append(Reservation)

     
#-------------------------------------------------------------------------------------------------#
#   Menu Item 4 : Show Booked Hotels                                                              #
#-------------------------------------------------------------------------------------------------#

def menu_item4():
    User_Input = ""
    while User_Input.lower() != "q":
        show_booked_hotels()
    
        print("\n#---------------------------#")
        print("# (R) For Retry  (Q) For Quit #")
        print("#-----------------------------#") 
        User_Input = input("\n")

       

def show_booked_hotels():
    
    if (gv_Booked_Hotels != []):
        for x in range (0, len(gv_Booked_Hotels)):
            print(f"\n\n{x + 1}. {gv_Booked_Hotels[x][0].upper()}")
     
    else:
        print("\n\nYou haven't booked a hotel yet")
        return gv_Booked_Hotels  

    while 1==1:
        Reservation_num = int(input("\nType the list number of revervation, you want to see: "))
        Hotel = Reservation_num - 1
        if(len(gv_Booked_Hotels) > Hotel):
            break

    
    print(f"\nReservationed Hotel: {gv_Booked_Hotels[Hotel][0].upper()}")
    print(f"Reservation Date: {gv_Booked_Hotels[Hotel][1]}/{gv_Booked_Hotels[Hotel][2]}/{gv_Booked_Hotels[Hotel][3]} {gv_Booked_Hotels[Hotel][4]}  11:00 am ")
    print(f"Room type: {gv_Booked_Hotels[Hotel][5]}")
    print(f"Cost: ${gv_Booked_Hotels[Hotel][6]}")
    return gv_Booked_Hotels

#-------------------------------------------------------------------------------------------------#
#   Menu Item 5 : Cancel Hotel Reservation                                                        #
#-------------------------------------------------------------------------------------------------#

def menu_item5():
    User_Input = ""
    while User_Input.lower() != "q":
        cancel_reservation()
        
        print("\n#---------------------------#")
        print("# (R) For Retry  (Q) For Quit #")
        print("#-----------------------------#") 
        User_Input = input("\n")

        
def cancel_reservation():

    print("You can cancel your reservations by typing it's number\n\n")
    print("If you don't want to delete your resarvation type 0")

    for x in range (0, len(gv_Booked_Hotels)):
        print(f"\n\n{x + 1}. {gv_Booked_Hotels[x][0].upper()}")

    Num = int(input("Please enter the number: ")) - 1

    if(Num == -1): return

    for x in range(0, len(gv_Booked_Hotels)):
        if(Num == gv_Booked_Hotels.index(gv_Booked_Hotels[x]) ):
            print(f"Your reservation in {gv_Booked_Hotels[x][0].upper()} is cancelled")
            gv_Booked_Hotels.remove(gv_Booked_Hotels[x])
            break

    return gv_Booked_Hotels
    
    
#-------------------------------------------------------------------------------------------------#
#   Print Main Menu                                                                               #
#-------------------------------------------------------------------------------------------------#

def Print_Main_Menu():
    Main_Menu_Textbody = """
        You can select menu options by typing their numbers.
        You can turn back to Main Menu just typing 'Q'.
        If you want to run the same option just type 'R'

        Welcome to Trip Planner 
        ------------------------
        1. Filter Hotels
        2. Look for Hotel 
        3. Book a Hotel
        4. My Booked Hotels
        5. Cancel Reservation
        6. Exit
        """
    print(Main_Menu_Textbody)


#-------------------------------------------------------------------------------------------------#
#   Load Data from Excel Sheet                                                                    #
#-------------------------------------------------------------------------------------------------#

def Load_Data_From_Excel():
    excel_file = "./Hotels.xlsx"
    wkb = openpyxl.load_workbook(filename= "Hotels.xlsx") 
    sheet = wkb.worksheets[0]

    gv_Hotels.clear()
    for row in range(2,sheet.max_row+1):
        new_row = []
        for col in range (1,sheet.max_column+1): 
            new_row.append(sheet.cell(row=row, column=col).value)
        gv_Hotels.append(new_row)

#-------------------------------------------------------------------------------------------------#
#   Main Entry Point                                                                              #
#-------------------------------------------------------------------------------------------------#

main()

#-------------------------------------------------------------------------------------------------#




