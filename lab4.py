
class File:

    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        data = {}
        antal_fel_rader = 0
        with open(self.filename, 'r') as h:
            for line in h:
                try:
                    four_vals = line.split(',')
                    batch = four_vals[0]
                    if not batch in data:
                        data[batch] = []
                    data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))]
                except:
                    antal_fel_rader += 1
            print('Din fil hade ' + str(antal_fel_rader) + ' rader med fel format, de hoppades över')
            return data
        

class Datapoints:
    
    def __init__(self, data):
        self.data = data
    
    def calculate(self):
        for batch, sample in self.data.items(): 
            if len(sample) > 0:
                n = 0
                x_sum = 0
                for (x, y, val) in sample:
                    if x**2 + y**2 <= 1:
                        x_sum += val
                        n += 1
                if x_sum > 0:
                    average = x_sum/n
                    print(batch, "\t", average)
                else:
                    print('Batch ' + batch + ' has no points inside the unit circle.')
            else:
                print(batch, "\tNo data")

    def print_data(self):
        pass


def main2():
    file = File('sample4.txt')
    data_dictionary = file.load_file()
    data = Datapoints(data_dictionary)
    data.calculate()
            
def main():
    '''
    This is the main body of the program.
    '''
    
    filename = input('Which data file? ')

    data = {}
    with open(filename, 'r') as h:
        for line in h:
            four_vals = line.split(',')
            batch = four_vals[0]
            if not batch in data:
                data[batch] = []
            data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))] # Collect data from an experiment

    for batch, sample in data.items(): 
        if len(sample) > 0:
            n = 0
            x_sum = 0
            for (x, y, val) in sample:
                if x**2 + y**2 <= 1:
                    x_sum += val
                    n += 1
            average = x_sum/n
            print(batch, "\t", average)
        else:
            print(batch, "\tNo data")


    


# Start the main program: This is idiomatic python
#if __name__ == '__main__':
    #main()

# The idea with this idiom is that if this code is loaded as a module,
# then the __name__ variable (internal to Python) is not __main__ and
# the body of the program is not executed. Consider what would happen
# if the main function was not in a function: an import statement (for
# example "import o4") would load the functions and then executed
# "filename = input(...)" and that is probably not what you want. The
# idiom is simply an easy way of ensuring that some code is only
# executed when run as an actual program.
#
# Try it out by importing this file into another project!
    