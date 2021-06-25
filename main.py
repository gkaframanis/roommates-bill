from bill import Bill
from filesharer import FileSharer
from roommate import Roommate
from reports import PdfReport

if __name__ == '__main__':
    # Get values from the user
    amount = float(input("Hey user, enter the bill amount: "))
    period = input("What is the bill period? E.g.: December 2020: ")
    bill = Bill(amount, period)

    name = input("What is your name? ")

    days_in_house = int(input(f"How many days did you, {name}, stay in the house during the bill period? "))

    while days_in_house > 31:
        print("The days you stayed in the house cannot be more than 31...")
        days_in_house = int(input(f"How many days did you, {name}, stay in the house during the bill period? "))

    roommate = Roommate(name, days_in_house)
    roommates_list = [roommate]

    answer = input("Type yes if you have to add another flatmate or no if there isn't another one: ")
    while answer.lower() == "yes":
        name = input("What is the flatmate's name? ")
        days_in_house = int(input(f"How many days did {name} stay in the house during the bill period? "))

        while days_in_house > 31:
            print("The days you stayed in the house cannot be more than 31...")
            days_in_house = int(input(f"How many days did {name} stay in the house during the bill period? "))

        roommate = Roommate(name, days_in_house)
        roommates_list.append(roommate)

        answer = input("Type 'yes' if you have to add another flatmate or if there isn't another one type 'no': ")

    *roommates, = roommates_list
    pdf_report = PdfReport(filename=f"bill_{bill.period}.pdf")
    pdf_report.generate(bill, *roommates)

    file_sharer = FileSharer(filepath=pdf_report.filename)
    # Prints the url of the uploaded file.
    print(file_sharer.share())
    exit(0)
