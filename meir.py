def increment_string(strng):
    num_intt = 0
    numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(strng) < 1:
        return '1'
    if strng[-1] in numb:
        for i in range(len(strng) - 1, -1, -1):
            if strng[i] in numb:
                num_intt += 1  # counts how many ints we have from the end
        # обрезать string, чтобы не было intов в конце
        str_noints = strng[:(-1 * num_intt)]

        nums = strng[-1:(-1 * num_intt - 1):-1]  # find int from the end
        nums = nums[::-1]  # reverse the int, while it is string
        zeros = 0
        for j in range(len(nums) - 1):  # find how many zeros we have in our int
            if nums[j] == '0':
                zeros += 1
        new_num = int(nums)  # our int
        final_num = new_num + 1  # output int
        if num_intt == len(str(final_num)):  # if new number equal to number of ints that we have
            zeros = 0
        elif num_intt > len(str(final_num)):
            zeros -= (num_intt - len(str(final_num)))

        final_str = str_noints + zeros * '0' + str(final_num)

        return final_str
    else:
        return strng + '1'


print(increment_string('foobar00999'))