def make_alphabetic_str(line=""):
    conv_list=list(line)
    new_list=[]
    for item in conv_list:
        if conv_list[item].isalpha():
             new_list.append(conv_list[item])
    new_str=str(new_list)
    return new_str


