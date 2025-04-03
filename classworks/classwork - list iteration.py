"""
(c) Masterschool
(c)2025 Justus Decker - coding solutions
"""

"""
Sacks of Gold
I’ve just robbed a bank 🏦. 
Here is a list of the weight of the sacks of gold I stole. 
How much do they weigh in total?
"""
sacks = [2.33, 4.1, 8.5, 6.66, 2.4]
total_weight = sum(sacks)

"""
The Escape
Oh no! the police is here! I need to get rid of some weight to run fast. How much will the sacks weigh if I throw away the ones that are heavier than 5kg? 😨 
Bad Luck
I have many pearl necklaces. However some of them bring bad luck. How many necklaces have 13 pearls in them? 🦪
"""

necklaces = [12, 13, 22, 18, 13, 10, 30, 15, 13, 12]
unlucky_pearls = necklaces.count(13)

"""
Common Names
Here is a list of common names. 👨🏽‍🦱👩🏽
How many of them start with “H”?
How many of them start with “L” and are 4 letters long?
"""
names = ["Emma", "Felix", "Henry", "Linn", "Lina", "Felix", "Hannah", "Noah", "Marie", "Leon"]

h_start = [name for name in names if name.lower().startswith("h")]
l_start_4 = [name for name in names if name.lower().startswith("l") and len(name) == 4]

"""
Warehouse
In the warehouse I have 8 big boxes, each one of them contains 4 medium sized boxes, each containing 6 small boxes. How many boxes do I have? 🏭
"""
boxes = [8, 4, 6]
all_boxes = 1
for i in boxes:
    all_boxes *= i
    
"""
Bonus: Class Average
I’ve finally finished grading all of my students tests. I wonder, what is the class average? 📑
"""
grades = [1.0, 2.1, 1.5, 3.0, 1.0, 1.2, 3.5, 1.0]
avg = round(sum(grades) / len(grades),1)

"""
Bonus: 5km Run
I go out running 5 km every day and record my time. What was my fastest run? 🏃🏽‍➡️
"""

times = [31.3, 29.8, 29.4, 30.3, 28.9, 29.4]
fastest = min(times)