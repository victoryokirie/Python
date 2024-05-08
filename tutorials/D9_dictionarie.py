##Dictionaries allow us to group together related pieces of information. A dictionary consist of key-pair values. Every dictionary has a key and a value to the key

# programming_dictionary = {
#     "Bug": "An unexpected error in a program that doesn't allow it run as intended", 
#     "Function": "A reusable piece of code",
# }

# #create an empty dictionary
# empty_dictionary = {}

# #loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# #edit an item in a dictionary
# programming_dictionary["Bug"] = "Its a bug"

# student_score = {
#     "Harry": 81,
#     "Hermione": 94,
#     "Daniel": 76,
#     "Nevvile": 82,
#     "James": 63
# }

# student_grade = {}

# for student in student_score:
#     score = student_score[student]

#     if score > 90:
#         student_grade[student] = "Outstanding"
#     elif score > 80:
#         student_grade[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grade[student] = "Acceptable"
#     else:
#         student_grade[student] = "Fail"

# print(student_grade)

#Nesting dictionaries and lists

nested_dictionary = {
    "List": [],
    "Dictionary": {},
} 

travel_log = {
    "France": {"cities_visited": ["Paris", "Merseille", "Dijon"], "total_visits": 12,},
    "Germany":{"cities_visited": ["Harmburg", "Dortmund", "Bayern"], "total_visits": 20}
}


travel_log2 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Merseille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany", 
        "cities_visited": ["Harmburg", "Dortmund", "Bayern"], 
        "total_visits": 20
    },
]

