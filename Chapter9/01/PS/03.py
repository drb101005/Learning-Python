#write a code to genrate tables from 2 to 20 , each of them in thier own file


def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"Chapter9/01/PS/tables/table_{n}.txt", "w") as f:
        f.write(table)




for i in range(2, 21):
    generateTable(i)