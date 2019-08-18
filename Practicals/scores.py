def main():
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    print(subjects)
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    print(score_values)
    for subject in range(len(subjects)):
        print(subjects[subject] + ", Scores:")
        max_num = 0
        min_num = 100
        total = 0
        avg_num = 0
        for i in range(len(score_values)):
            print(score_values[i][subject])
            if score_values[i][subject] > max_num:
                max_num = score_values[i][subject]
            if score_values[i][subject] < min_num:
                min_num = score_values[i][subject]
            total += score_values[i][subject]
            avg_num = total/10

        print("Max: " + str(max_num))
        print("Min: " + str(min_num))
        print("Average: " + str(avg_num))


main()