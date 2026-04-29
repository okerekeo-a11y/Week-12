"""
Ogechukwu Okereke
CMSC 111
Week 12 Assignment - Dice Simulator
"""
import random
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"Dice 1 rolled: {die1}")
print(f"Dice 2 rolled: {die2}")
total = math.fsum([die1, die2])
print(f"Total: {int(total)}")
image1 = mpimg.imread(f"dice_{die1}.png")
image2 = mpimg.imread(f"dice_{die2}.png")
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plt.imshow(image1)
plt.axis("off")
plt.title(f"Dice 1: {die1}")
plt.subplot(1, 2, 2)
plt.imshow(image2)
plt.axis("off")
plt.title(f"Dice 2: {die2}")
plt.show()
