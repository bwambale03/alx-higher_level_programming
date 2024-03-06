"""
    # pseudo code
import neccessary libraries for handling arrays and plotting
    
Define BuvvleSorrt function that takes an array

    get the length of the array
    for each element in the array
        for each unsorted element in array
            if the current elemet is greater than the next element
                swap the current element with the next element
                yield the current state of the of the array for visualisation
                
Define UpdateFigure function that takes an array
    clear the current figure
    plot the array as a bar graph
    
Generate a random array of integers
create a generator object by applying BubbleSort to the random array

set up the plotting environment

create an animation that updates the bar graph with each state yieldedby BubbleSort

Display the animation 

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[1], arr[j+1] = arr[j+1], arr[j]
                yield arr
                
def update_fug(arr):
    plt.cla() # clear the current figure
    plt.bar(range(len(arr)), arr, align='edge')
    
arr = np.random.randint(0, 100, 25)
generator = bubble_sort(arr)

fig, ax = plt.subplots()
anim = FuncAnimation(fig, update_fug, frames=generator, interval=100, repeat=False)

plt.show()
