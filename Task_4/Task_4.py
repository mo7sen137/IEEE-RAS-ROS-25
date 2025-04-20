#Problem 1
#Create a program that reads a text file, counts the occurrences of each word, and prints the results
def main():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as file:
            word_count = {}
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower()
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        
            print("\nWord counts:")
            for word, count in word_count.items():
                print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please check:")
        print("1. The file exists in the same folder as this program")
        print("2. You've typed the name correctly with extension (e.g. 'text.txt')")
    except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()



#Problem 2
#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line
def main():
    students = []
    total=int(input(f"Enter the total num of students: "))
    for _ in range (total) :
        name = str(input(f"Enter name: "))
        score = float(input(f"Enter the score: "))
        students.append([name, score])
    unique_scores = sorted(set(score for name, score in students))
    
    second_lowest = unique_scores[1] if len(unique_scores) > 1 else None
    
    result = sorted([name for name, score in students if score == second_lowest])
    
    for name in result:
        print(name)

if __name__ == "__main__":
    main()




#Problem 3
#Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

def main():
    lst = []
    n = int(input(f"Enter num of commands: "))
    for _ in range(n):
        command = input(f"Enter the command: ").split()
        
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()

if __name__ == "__main__":
    main()





#Problem 4
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.



def main():
    n = int(input(f"Enter the num of Scors: "))  
    scores = list(map(int, input().split()))  
    
    unique_scores = sorted(list(set(scores)), reverse=True)
    
    print(unique_scores[1])


if __name__ == "__main__":
    main()








#Problem 5
#You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help! A valid credit card from ABCD Bank has the following characteristics:


import re
def main():
    def is_valid_credit_card(card_number):
        if not re.match(r'^[456]', card_number):
            return False

        digits = card_number.replace('-', '')
        if len(digits) != 16 or not digits.isdigit():
            return False
    
    
        if '-' in card_number:
            if not re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card_number):
                return False
    
    
        if re.search(r'(\d)\1{3,}', digits):
            return False
    
    return True

if __name__ == '__main__':
    n = int(input(f"Enter num of cards: "))
    for _ in range(n):
        card = input(f"Enter card num: ").strip()
        if is_valid_credit_card(card):
            print('Valid')
        else:
            print('Invalid')


#Problem 6
# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them


import datetime
def parse_timestamp(timestamp):
    parts = timestamp.split()
    day_name = parts[0]
    day = int(parts[1])
    month = parts[2]
    year = int(parts[3])
    time = parts[4]
    timezone = parts[5]
    
    hours, minutes, seconds = map(int, time.split(':'))
    
    tz_sign = timezone[0]
    tz_hours = int(timezone[1:3])
    tz_minutes = int(timezone[3:5])
    
    month_num = datetime.datetime.strptime(month, '%B').month
    dt = datetime.datetime(year, month_num, day, hours, minutes, seconds)
    
    tz_offset = (tz_hours * 3600 + tz_minutes * 60)
    if tz_sign == '-':
        tz_offset = -tz_offset
    
    dt = dt - datetime.timedelta(seconds=tz_offset)
    
    return dt

if __name__ == '__main__':
    T = int(input(f"Enter the number of testcases: "))
    for _ in range(T):
        t1 = input().strip()
        t2 = input().strip()
        
        dt1 = parse_timestamp(t1)
        dt2 = parse_timestamp(t2)
        
        diff = abs(int((dt1 - dt2).total_seconds()))
        print(diff)





