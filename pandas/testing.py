
if __name__ == "__main__":
    x = [{"hello":3,"world":1},{"hello":1}]

    var_dict = dict()

    for i in x:
        for j in i.keys():
            if j not in var_dict:
                var_dict[j] = i[j]
            else:
                var_dict[j] += i[j]

    print(var_dict)



