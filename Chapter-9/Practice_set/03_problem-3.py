# Q-3 Write a program to generate multiplication tables from 2 to 20 and write it to the  different files. Place these files in a folder for a 13 – year old.


def multi_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"Chapter-9/Practice_set/table/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    multi_table(i)
