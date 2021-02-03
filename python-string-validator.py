import re


def flou_string_only_alpha_num_space(ini_string):
    # keeps only letters, numbers and space and uses strip() and removes multiple spaces
    # there is a joker for spaces
    joker = "69xx686"
    ini_string = ini_string.strip()
    ini_string = re.sub(' +', ' ', ini_string)
    ini_string = ini_string.replace(" ", joker)
    result = re.sub('[\W_]+', '', ini_string)
    result = result.replace(joker, " ", )
    result = re.sub(' +', ' ', result)
    return result


def flou_str_start_letter(ini_string):
    #  prefixes with x if if the string starts with a number
    if ini_string[0].isnumeric():
        ini_string = "z" + ini_string
    return ini_string


# *********************** TEST ZONE BELOW ***********************
# def flou_test():
#     ini_string = "     123     aBcjw:, .@! .@!.@!.@!.@!.@!.@!.@!.@!e :, .@! .@!.@!.@!.@!.@!.@!.@!.@!e :, .@! .@!.@!.@!.@!.@!.@!.@!.@!e    iw"
#     print("initial string : ", ini_string)
#     result = flou_string_only_alpha_num_space(ini_string)
#
#     print("final string", result)
#
# flou_test()
print(flou_str_start_letter("pl"))
