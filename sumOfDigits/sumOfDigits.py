class BaseConverter:
    def __init__(self, n_str, num_bases):
        self.n_str = n_str
        self.n = int(n_str)
        self.num_bases = num_bases
        self.base_list = []
        self.setBaseDict()

    def setBaseDict(self):
        self.base_list.append([])  # base zero is nonsensical
        self.base_list.append([])  # base one is nonsensical
        for base in range(2, num_bases + 2):
            self.base_list.append([])
            base_list = self.base_list[base]
            remaining_n = self.n
            digit_num = 0
            while remaining_n != 0:
                base_list.append(remaining_n % base)
                remaining_n = remaining_n // base
                digit_num += 1

    def displayResults(self):
        for base in range(2, num_bases + 2):
            print_str = str(base) + ':\t'
            base_list = self.base_list[base]
            last_idx = len(base_list) - 1
            digit_sum = 0
            for digit_num, digit in enumerate(reversed(base_list)):
                digit_sum += digit
                print_str += str(digit)
                if digit_num != last_idx:
                    print_str += ', '
                else:
                    print_str += '\t' + str(digit_sum)
            print(print_str)

if __name__ == '__main__':
    n_str = input('Input n: ')
    num_bases = int(input('Input number of bases to compute: '))
    bc = BaseConverter(n_str, num_bases)
    bc.displayResults()
