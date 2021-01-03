#(Hard)

id_1 = "#4"
average_grade_1 = "A"
test_score_1= 90

id_2 = "#5"
average_grade_2 = "A"
test_score_2 = 70

no_duplicates = id_1 != id_2
print("No duplicate entries:")
print(no_duplicates)

same_average = average_grade_1 == average_grade_2
print("Same average grade:")
print(same_average)

higher_score = test_score_1 > test_score_2
print("id_1 has a higher score:")
print(higher_score)
