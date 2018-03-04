from collections import Counter
text="In geometry, parallel lines are lines in a plane which do not meet; that is, two lines in a plane that do not intersect or touch each other at any point are said to be parallel. By extension, a line and a plane, or two planes, in three-dimensional Euclidean space that do not share a point are said to be parallel."
words=text.split()
print(words)

counter=Counter(words)
top_three=counter.most_commmon(3)
print(top_three)