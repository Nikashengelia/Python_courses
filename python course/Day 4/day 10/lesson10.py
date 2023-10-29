nums = [2, 4, 6, 2, 4, 7, 2, 9]
while 4 in nums:
    nums.remove(4)
print(nums)




####### meore davaleba
family = ["Lana", "Kaxa", "Luka"]
ages = [36, 38, 10]
current_ages = "My mom's name is {}, she is {} years old. My father's name is {}, he is {} years old. My brother's name is {}, he is {} years old.".format(family[0], ages[0], family[1], ages[1], family[2], ages[2])
ages_in_10_years = [age + 10 for age in ages]
ages_in_10_years_ = "In 10 years, my mom will be {}, my father will be {}, and My brother will be {}.".format(ages_in_10_years[0], ages_in_10_years[1], ages_in_10_years[2])
print(current_ages)
print(ages_in_10_years_)