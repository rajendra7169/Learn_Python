# Index in python
# String is immutable which means we cant not change it
name = "Raja"  # 0=R, 1=a, 2=j, 3=a and -1=a, -2=j

# len is a default funcation which counts the cheracter

shortname = name[3], len(name)


print(shortname)

print(name[0:3])  # THis prints cheracters from 0 to 3 which is R,a and j

print(name[1:])  # This is same as [1:3]
print(name[:3])  # This is same as [0;3]

word = "amazing"
print(word[1:6:2])  # Resukt will be 'mzn' becacue this jump by 2
