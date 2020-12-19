import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def is_prime(number):
    """A prime number is a number that is only evenly divisble by itself and 1.
    For example, the number 5 is prime because it can only be evenlly divided by 1
    and 5. The number 6, however, is not prime because it can be divided evenly
    by 2 and 3."""
    #number will be a prime number if the remainder is 0 only 2 times when then number is divided by 1 until itself
    #initialize variable to count the remainder being 0
    count = 0
    for i in range (1,number+1):
        is_prime = number % i
        if is_prime == 0:
            count += 1        
        else: count = count
        i += 1
    if count == 2:
        return True
    elif count > 2:
        return False


frequencies = 0
values = 0
prime_list = [] #list to store the prime numbers

# Generate a list of prime numbers between 1000 and 1050 (inclusive) which has 10000 runs
for i in range(0,10000):
    number = random.randrange(1000, 1051)
    if is_prime(number) == True:
        prime_list.append(number)

#count the frequencies and values in a tuple using numpy unique and return_counts
values, frequencies = np.unique(prime_list, return_counts=True)
#print(values, frequencies)

#Creating the inital bar plot
title = 'Frequency of prime numbers between 1000 and 1050'
sns.set_style('whitegrid')
axes = sns.barplot(x = values, y = frequencies, palette = 'bright')

#SEtting the window title and labeling the x and y axes
axes.set_title(title)
axes.set(xlabel = 'Prime Number', ylabel = 'Frequency')

#Finalizing the bar plot
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(prime_list):.3%}'
    axes.text(text_x, text_y, text, fontsize = 11, ha = 'center', va = 'bottom')

plt.show()

#End