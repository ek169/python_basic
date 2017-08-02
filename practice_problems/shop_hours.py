
input1 = [
    ['9:00', '5:00'], # Monday
    ['9:00', '5:00'], # Tuesday
    ['9:00', '5:00'], # ...
    ['9:00', '5:00'],
    ['9:00', '5:00'],
    ['9:00', '5:00'],
    ['9:00', '5:00'],
]
expected1 = [
    'Monday - Sunday: 9:00 - 5:00'
]


input2 = [
    ['9:00', '5:00'], # Monday
    ['9:00', '5:00'], # Tuesday
    ['9:00', '5:00'], # ...
    ['9:00', '5:00'],
    ['9:00', '5:00'],
    ['12:00', '5:00'],
    ['12:00', '5:00'],
]
expected2 = [
    'Monday - Friday: 9:00 - 5:00',
    'Saturday - Sunday: 12:00 - 5:00'
]


input3 = [
    ['8:00', '4:00'], # Monday
    ['9:00', '5:00'], # Tuesday
    ['8:00', '4:00'], # ...
    ['9:00', '5:00'],
    ['8:00', '4:00'],
    ['12:00', '5:00'],
    ['12:00', '5:00'],
]
expected3 = [
    'Monday, Wednesday, Friday: 9:00 - 5:00',
    'Tuesday, Thursday: 8:00 - 4:00',
    'Saturday - Sunday: 12:00 - 5:00'
]


input4 = [
    ['8:00', '4:00'], # Monday
    ['8:00', '5:00'], # Tuesday
    ['8:00', '4:00'], # ...
    ['9:00', '5:00'],
    ['8:00', '4:00'],
    ['12:00', '5:00'],
    ['12:00', '5:00'],
]
expected4 = [
    'Monday, Wednesday, Friday: 8:00 - 4:00',
    'Tuesday: 8:00 - 5:00',
    'Thursday: 9:00 - 5:00',
    'Saturday - Sunday: 12:00 - 5:00',
]



the_input = input1

dictionary = dict()
hours_list = []
days_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6:"Sunday"}
for i in range(len(the_input)):
    if the_input[i][0] + ',' + the_input[i][1] not in dictionary.keys():
        dictionary[the_input[i][0] + ',' + the_input[i][1]] = [i]
    else:
        dictionary[the_input[i][0] + ',' + the_input[i][1]].append(i)
for i in dictionary:
    times = i.split(',')
    if int(times[0][0]) < 12:
        open_time = times[0] + ' a.m. - '
    else:
        open_time = times[0] + ' p.m. - '
    close_time = times[1] + ' p.m.'
    hours = open_time + close_time

    the_string = ""
    if len(dictionary[i]) == 1:
        the_string += days_of_week[dictionary[i][0]] + ": " + hours
    else:
        k = 1
        while k < len(dictionary[i]):
            if dictionary[i][k] == dictionary[i][k-1] + 1:
                the_string += days_of_week[dictionary[i][k-1]] + '-'
                j = k
                while j < len(dictionary[i]):

                    if (dictionary[i][j] == dictionary[i][j-1] + 1) and (j is not len(dictionary[i])-1):
                        j += 1
                    else:
                        the_string += days_of_week[dictionary[i][j]] + ": " + hours
                        j += 1
                        k = j

            else:
                if k+1 == len(dictionary[i]):
                    the_string += days_of_week[dictionary[i][k]] + ": " + hours
                else:
                    m = k - 1
                    while m < len(dictionary[i])-1:
                        if dictionary[i][m] is not dictionary[i][m+1] - 1:
                            the_string += days_of_week[dictionary[i][m]] + ', '
                        else:
                            k = m
                            break
                        m += 1
                k += 1

    hours_list.append(the_string)

for day in days_of_week.values():
    for lt in hours_list:
        if day in lt:
            print(lt)
            hours_list.remove(lt)
