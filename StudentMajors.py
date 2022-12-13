def group_by_owners(files):
    results = {}
    for i in files:
        if files[i] in results.keys():
            results[files[i]].append(i)
        else:
            results[files[i]] = [i]
        # print(files[i])
    return results

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }  

    print(group_by_owners(files))