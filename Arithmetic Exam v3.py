while True:
    dif_level = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
""")

    if int(dif_level) == 1 or int(dif_level) == 2:
        break
    else:
        print("Incorrect format.")
        continue

mark = 0
task_no = 0

while task_no < 5:
    import random
    if int(dif_level) == 1:
        oper_list = ["+","-","*"]
        first_n = str(random.choice(range(2,10)))
        second_n = str(random.choice(range(2,10)))
        oper = random.choice(oper_list)

        print(f"{first_n} {oper} {second_n}")
        result = eval(first_n + oper + second_n)

        level_exp = "simple operations with numbers 2-9"

    elif int(dif_level) == 2:
        first_n = int(random.choice(range(11,30)))
        result = first_n ** 2
        level_exp = "integral squares of 11-29"

        print(str(first_n)) 
    while True:
        try: 
            user_calc = int(input())
        except ValueError:
            print("Wrong format! Try again.")
            continue
        else:
            break

    print("Right!") if user_calc == result else print("Wrong!")
        
    if user_calc == result:
        mark += 1
    task_no += 1  

print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
memo = input()

if memo == "yes" or memo == "YES" or memo == "Y" or memo == "y":
    print("What is your name?")
    name = input()
    results_f = open("results.txt", "a", encoding = "utf-8")
    results_f.write(f"{name}: {mark}/5 in level {dif_level} ({level_exp}).")
    results_f.close()
    
    print('The results are saved in "results.txt".')

else:
    exit()
