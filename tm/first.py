if __name__ == '__main__':
    first_list = []
    second_list = []
    print("შემოიყვანეთ რიცხვები: ")
    for i in range(10):
        a = int(input())
        first_list.append(a)

    with open("MyNumber.txt", "r") as f:
        for i, ind in enumerate(f.readlines()):
            second_list.append(int(ind))

    min1 = 99999999
    max1 = -99999999
    min2 = 99999999
    max2 = -99999999

    for i in range(len(first_list)):
        if first_list[i] < min1:
            min1 = first_list[i]
        if first_list[i] > max1:
            max1 = first_list[i]

    for i in range(len(second_list)):
        if second_list[i] < min2:
            min2 = second_list[i]
        if second_list[i] > max2:
            max2 = second_list[i]

    print("მინიმუმი შემოყვანილთაგან:", min1)
    print("მაქსიმუმი შემოყვანილთაგან:", max1)
    print("მინიმუმი ფაილიდან:", min2)
    print("მაქსიმუმი ფაილიდან:", max2)
    print("გაფანტულობის დიაპაზონი შემოყვანილთათვის:", max1 - min1)
    print("გაფანტულობის დიაპაზონი ფაილიდან:", max2 - min2)

    sum1 = 0
    sum2 = 0

    for i in range(len(first_list)):
        sum1 += first_list[i]
    for i in range(len(second_list)):
        sum2 += second_list[i]

    print("საშუალო შემოყვანილთათვის:", sum1 / len(first_list))
    print("საშუალო ფაილიდან:", sum2 / len(second_list))

    freq1 = {}
    freq2 = {}
    max_freq1 = 0
    max_freq2 = 0
    for i in range(len(first_list)):
        if first_list[i] in freq1:
            freq1[first_list[i]] += 1
        else:
            freq1[first_list[i]] = 1
    for i in range(len(second_list)):
        if second_list[i] in freq2:
            freq2[second_list[i]] += 1
        else:
            freq2[second_list[i]] = 1

    for i in first_list:
        if freq1[i] > max_freq1:
            max_freq1 = i
    for i in second_list:
        if freq2[i] > max_freq2:
            max_freq2 = i

    print("მოდა შემოყვანილთათვის:", max_freq1)
    print("მოდა ფაილისთვის:", max_freq2)
    print("მედიანა შემოყვანილთათვის:", first_list[int(len(first_list) / 2)])
    print("მედიანა შემოყვანილთათვის:", second_list[int(len(second_list) / 2)])

    with open("reports.txt", "w") as f:
        if len(second_list) > len(first_list):
            f.write(f"მეორე მიმდევრობა მეტია პირველ მიმდევრობაზე: {len(second_list) - len(first_list)} - ით")
        if len(first_list) > len(second_list):
            f.write(f"პირველი მიმდევრობა მეტია მეორე მიმდევრობაზე: {len(first_list) - len(second_list)} - ით")
        if len(first_list) == len(second_list):
            f.write(f"პირველი მიმდვერობა და მეორე მიმდევრობა ტოლებია")
        f.write("\n")
        f.write("პირველი მიმდევრობის სიგრძე: " + str(len(first_list)))
        f.write("\n")
        f.write("მეორე მიმდევრობის სიგრძე: " + str(len(second_list)))
