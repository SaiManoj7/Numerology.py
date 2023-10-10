numerology_values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8, ' ':0
}

#Moolank is sum of Digit of day of months 
#Exception is 11, 22, 
def getMoolank(birth_date):
    moolank = (int(birth_date))%9
    return moolank if moolank!=0 else 9

def personal_year(born_date, born_month, Predicted_year):
    total = born_date + born_month + Predicted_year
    return total if total!=0 else 9


def personal_month_number(born_date, born_month, present_year):
    born_date_str = str(born_date)
    born_date_number = 0

    for digit in born_date_str:
        born_date_number += int(digit)

    personal_year_number = born_date_number + born_month + present_year
    personal_month_number = (personal_year_number)%9
    return personal_month_number if personal_month_number!=0 else 9

def personal_day_number(born_date, born_month, present_date, present_month, present_year):

    def digit(number):
        if number % 9 == 0:
            return 9
        return number % 9

    born_date = digit(born_date)
    born_month = digit(born_month)
    present_date = digit(present_date)
    present_month = digit(present_month)
    present_year = digit(present_year)

    day_number = digit(born_date + born_month + present_date + present_month + present_year)
    return day_number

def getDestinyNumber(full_name):

    # Converting the full name into uppercase and calculating the total
    total = 0
    for char in full_name:
        if char.isalpha():
            total += numerology_values[char.upper()]
    total = total%9
    return total if total!=0 else 9

def compatible_number(Person_1, Person_2):
    # Adding  Life Path Numbers
    life_path_sum = Person_1['LifePathNumber'] + Person_2['LifePathNumber']

    # Adding Destiny Numbers
    destiny_sum = Person_1['DestinyNumber'] + Person_2['DestinyNumber']

    # total sum
    total_sum = (life_path_sum + destiny_sum)%9
    return total_sum if total_sum !=0 else 9


def life_path_number(birthdate):

    components = birthdate.replace("-", "") #30-10-2002
    Destiny_number = (sum(map(int, components)))%9
    return Destiny_number if Destiny_number !=0 else 9

"""
Method: add the pythagorian value of the initials of your full name at birth, first, middle and last initials 
then reduce them to a single digit, even if it is master number
Uses: Your Balance number provides guidance on how to best deal with difficult situations.
Source: https://www.worldnumerology.com/numerology-balance-number/

"""
def getBalanceNumber(name):
    name = name.upper()
    name = name.split(" ")
    numerology_value = 0
    for letter in name:
        if letter[0] in numerology_values:
            numerology_value += numerology_values[letter[0]]
    numerology_value = numerology_value%9
    return numerology_value if numerology_value !=0 else 9


def birth_month_numerology(birth_month):
    try:
        birth_month = int(birth_month)
        if birth_month < 1 or birth_month > 12:
            raise ValueError("Month should be between 1 and 12.")
    except ValueError:
        return "Invalid input. Please enter a valid month number (1-12)."
    birth_month = birth_month%9
    return birth_month if birth_month !=0 else 9


# **************Final Exposed Functions*********************** 
def getNumerologyReport(date_dd, date_mm, birthdate_str,fullName):
    # Test case
    birth_date = date_dd
    moolank = getMoolank(birth_date)
    birthMonth = birth_month_numerology(date_mm)
    destiny_number = getDestinyNumber(fullName)
    lifePathNumber = life_path_number(birthdate_str)
    balance_number = getBalanceNumber(fullName)

    return {'moolank':moolank,"birthMonth":birthMonth,"destinyNumber":destiny_number,"lifePathNumber":lifePathNumber, "balanceNumber":balance_number}

print(getNumerologyReport("22","5","22-5-2002","Alok Trivedi"))


def getPersonalYearMonthDay(born_date, born_month, Predicted_year,present_month,present_date):
    year = personal_year(born_date, born_month, Predicted_year)
    month = personal_month_number(born_date, born_month, Predicted_year)
    day = personal_day_number(born_date, born_month, present_date,present_month, Predicted_year)
    return {"personalYear":year, "personalMonth":month,"personalDay":day}


#Testing Compatible Number
Person_1 = {'LifePathNumber': 5, 'DestinyNumber': 8 }
Person_2 ={'LifePathNumber': 3, 'DestinyNumber': 6 }

compatible_number = compatible_number(Person_1, Person_2)





def getMasterNumber(born_date):
    born_year, born_month, born_day = map(int, born_date.split('-'))
    if born_month in [11, 22, 33] or born_day in [11, 22, 33] or born_year in [11, 22, 33]:
        return "Your numerology birth number is a master number."

    # Calculating the numerology birth number
    born_number = (sum(map(int, str(born_month))) + sum(map(int, str(born_day))) + sum(map(int, str(born_year)))) % 9
    return born_number if born_number != 0 else 9




def getEvilNumber(number):
    number=number%9
    number=number if number !=0 else 9
    return number in [2, 4, 6, 8]

# Input
"""number = int(input("Enter a number: "))

# if the number is evil or not
if getEvilNumber(number):
    print("The given number is", number,"and is a evil number.")
else:
    print("The given number is", number,"and is a (Lucky/Neutral).")"""


def getRulingNumber(born_date):
    total = sum(int(digit) for digit in born_date) % 9
    return total if total !=0 else 9
    

"""born_date = input("Enter your birth date (e.g., 1551990): ")
ruling_number = getRulingNumber(born_date)
print("Your ruling number is:", ruling_number)"""


def getExpressionNumber(name):
    name = name.upper()
    expression_number = 0
    
    for letter in name:
        if letter in numerology_values:
            expression_number += numerology_values[letter]

    expression_number = expression_number % 9
    return expression_number if expression_number != 0 else 9

def getLifePathNumber(birthdate):
    components = birthdate.replace("-", "") #30-10-2002
    Destiny_number = (sum(map(int, components)))%9
    return Destiny_number if Destiny_number !=0 else 9

def getMaturityNumber(life_path_number, expression_number):
    maturity_number = life_path_number + expression_number
    maturity_number = maturity_number % 9
    return maturity_number if maturity_number != 0 else 9

# Example usage
name = input("Enter your name: ")
date_of_birth = input("Enter your date of birth (in format YYYY-MM-DD): ")

expression_number = getExpressionNumber(name)
life_path_number = getLifePathNumber(date_of_birth)
maturity_number = getMaturityNumber(life_path_number, expression_number)

print(name,"has a Life Path Number of ",life_path_number)
print(name,"has an Expression Number of ",expression_number)
print("The Maturity Number for",name," is",maturity_number)


def getCornerStone(name):
    if name.isalpha() and name:
        first_letter = name[0].upper()
        cornerstone = ord(first_letter) - ord('A') + 1 
        cornerstone = cornerstone % 9 
        return cornerstone if cornerstone != 0 else 9 
    return None



def getCapestone(name):
    if name.isalpha() and name:
        last_letter = name[-1].upper()
        return last_letter
    return None




def getSoulUrgeNumber(name):
    vowel_values = {'A': 1, 'E': 5, 'I': 9, 'O': 6, 'U': 3}
    soul_urge_sum = 0
    
    name = name.upper()
    
    for char in name:
        if char in vowel_values:
            soul_urge_sum += vowel_values[char]
    
    
    soul_urge_number = soul_urge_sum % 9
    return soul_urge_number if soul_urge_number != 0 else 9


def getRationalThoughtNumber(complete_name, born_date):
    name_value = sum(ord(letter.lower()) - ord('a') + 1 for letter in complete_name if letter.isalpha())
    rational_thought_number = name_value + born_date

    rational_thought_number=rational_thought_number%9
    return rational_thought_number if rational_thought_number !=0 else 9


def getLifePathNumber(birthdate):
    components = birthdate.replace("-", "")
    destiny_number = (sum(map(int, components))) % 9
    karmic_debt_numbers = [13, 14, 16, 19]
    if destiny_number in karmic_debt_numbers:
        return destiny_number
    return destiny_number if destiny_number != 0 else 9


def getDreamNumber(full_name):
    char_value = sum(numerology_values.get(letter.lower(), 0) for letter in full_name if letter.isalpha())
    char_value = char_value % 9
    return char_value if char_value != 0 else 9


def getHiddenPassionNumber(full_name):
    nameofvalue = sum(numerology_values.get(letter.lower(), 0) for letter in full_name if letter.isalpha())
    nameofvalue = nameofvalue % 9
    return nameofvalue if nameofvalue != 0 else 9

def getUniversalDay(date):
    month, day, year = map(int, date.split('-'))
    sum_of_date= month + day + year
    sum_of_date = sum_of_date % 9
    return sum_of_date if sum_of_date !=0 else 9

def getUniversalMonth(universal_year, month):
    universal_year = int(universal_year)
    month = int(month)
    sum_of_month = universal_year + month
    sum_of_month = sum_of_month % 9
    return sum_of_month if sum_of_month !=0 else  9

def getUniversalYear(universal_year):
    universal_year= universal_year % 9
    return universal_year if universal_year !=0 else 9

def getPersonalYear(born_month, born_day, current_year):
    sum = int(born_month) + int(born_day)
    personal_year = sum + current_year
    personal_year=personal_year%9
    return personal_year if personal_year !=0 else 9
