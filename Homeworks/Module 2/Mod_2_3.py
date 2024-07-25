my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
m_l_zero = 0
while m_l_zero < len(my_list):
    if my_list[m_l_zero] < 0:
        break
    elif my_list[m_l_zero] > 0:
        print(my_list[m_l_zero])
    m_l_zero += 1