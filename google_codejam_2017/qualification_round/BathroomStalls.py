def main():
    output_file = open("/home/koofu/PycharmProjects/CodeJam/output.out", 'w')

    with open("/home/koofu/PycharmProjects/CodeJam/C-small-2-attempt0.in", 'r') as f:
        test_cases = f.readline().strip()
        for counter, rawline in enumerate(f):
            if counter+1 > int(test_cases):
                break
            line = rawline.strip()
            output_file.write("Case #{0}: {1}".format(counter+1, solve(line)+'\n'))


def solve(stripped_line):
    split_line = stripped_line.split()
    queue = list()
    queue.append(int(split_line[0]))
    for i in range(int(split_line[1])):
        queue.sort(reverse=True)
        value = queue.pop(0) - 1
        max_num = value//2
        holder = (max_num)+((value)%2)
        if holder == 0:
            return "0 0"
        queue.append(holder)
        queue.append(max_num)
    return "{0} {1}".format(queue[-2], queue[-1])


if __name__ == "__main__":
    main()
