# ASSGNMNT18

Python Basic 18

Q1.Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'.



from google.colab import files
uploaded = files.upload()
     
Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
Saving zoo.py to zoo.py

import zoo
from importlib import reload
reload(zoo)

zoo.hours()
     
Open 9-5 daily

Q2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.


import zoo as menagerie
menagerie.hours()
     
Open 9-5 daily

Q3. Using the interpreter, explicitly import and call the hours() function from zoo.


from zoo import hours
hours()
     
Open 9-5 daily

Q4. Import the hours() function as info and call it.


from zoo import hours as info
info()
     
Open 9-5 daily

Q5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, 'c': 3, and print it out.


plain = {'a': 1, 'b': 2, 'c': 3}
plain
     
{'a': 1, 'b': 2, 'c': 3}

Q6. Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?


#Yes
from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy
     
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

Q7. Make a defaultdict called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a']


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']
     
['something for a']


     
