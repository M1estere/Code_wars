def meeting(s):
    s_list = s.split(";")

    persons_result = []

    for i in range(0, len(s_list)):
        s_list_person = s_list[i].split(":")
        s_list_person.reverse()
        result_person_list = ", ".join(s_list_person)

        persons_result.append("(" + result_person_list.upper() + ")")

    result_string = ""

    for el in sorted(persons_result):
        result_string += el

    return result_string