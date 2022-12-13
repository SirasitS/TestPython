def unique_names(names1, names2):
    combine = names1 + names2
    # print(str(sorted(set(combine))))
    return sorted(set(combine))

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia