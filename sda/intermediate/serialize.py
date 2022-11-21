import pickle


def write_pickle(file_name):
    data = {
        'a': [1, 2.0, 3, 4+6j],
        'b': ("Alice has a cat", "Python programming is great"),
        'c': [False, True, False]
    }

    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def read_pickle(file_name):
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
    return data


if __name__ == '__main__':
    command = input("Do you want to read or write? ")
    if command == 'write':
        write_pickle('data_new.pickle')
        print("Saved data on disk")
        exit(0)
    elif command == 'read':
        file_data = read_pickle('data.pickle')
        # procesare, writ_pickle
        for name, age in file_data.items():
            print(name, age)
        print("retrieved data!")
