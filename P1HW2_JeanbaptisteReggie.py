Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Budget and Expense Tracker')
Budget and Expense Tracker
>>> print('24SEP2023')
24SEP2023
>>> print('CTI-110 P1HW2-Travel Expense')
CTI-110 P1HW2-Travel Expense
>>> print('Reggie Jean Baptiste')
Reggie Jean Baptiste
>>> budget=int(input('Enter the budget:'))
Enter the budget:3000
>>> destination=input('Enter Your destination:')
Enter Your destination:Mexico
>>>  gas=int(input('Enter amount that you will spend on gas:'))
  File "<stdin>", line 1
    gas=int(input('Enter amount that you will spend on gas:'))
IndentationError: unexpected indent
>>> gas=int(input('Enter amount that you will spend on gas:'))
Enter amount that you will spend on gas:500
>>> accomodation=int(input('Enter amount that you will spend on accomodation:'))
Enter amount that you will spend on accomodation:1500
>>> food=int(input('Enter amount that you will spend on food:'))
Enter amount that you will spend on food:300
>>> expenses=gas+accomodation+food
>>> result=budget-expenses
>>> print('You will have this amount left after expenses are deducted from your budget for your',destination,'trip is:',result)
You will have this amount left after expenses are deducted from your budget for your Mexico trip is: 700
>>> print("The result after subtracting your expenses from your budget for your",destination,"trip is:",result)
The result after subtracting your expenses from your budget for your Mexico trip is: 700
>>>
