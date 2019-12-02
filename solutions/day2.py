def run_proc(a, pc = 0):
    while True:
        inst = a[pc]
        if (inst == 99):
            return a
        elif (inst == 1):
            a[a[pc+3]] = a[a[pc+1]] + a[a[pc+2]]
            pc += 4
        elif (inst == 2):
            a[a[pc+3]] = a[a[pc+1]] * a[a[pc+2]]
            pc += 4
        else:
            raise Exception("unknown opcode")

def read_file_as_intcode(fname):
    with open(fname, 'r') as f:
        return list(map(int, f.read().split(',')))

def main():
    # part 1

    original = read_file_as_intcode("input2")
    # intcode = [1, 0, 0, 0, 99]
    # intcode = [2, 3, 0, 3, 99]
    # intcode = [2, 4, 4, 5, 99, 0]
    # intcode = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    # print(run_proc(intcode))

    # part 2
    for i in range(100):
        for j in range(100):
            copy = original.copy()
            copy[1] = i
            copy[2] = j

            if (run_proc(copy)[0] == 19690720):
                print(100 * i + j)
                return


if __name__ == "__main__":
    main()
