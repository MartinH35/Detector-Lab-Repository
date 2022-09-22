import argparse #this section of code allows the user to define the range of values for the calculation 
parser = argparse.ArgumentParser(description='FizzBuzz Game')
parser.add_argument('first_in_range',type=int,help='Enter the first number in the range')
parser.add_argument('last_in_range',type=int,help='Enter the last number in the range')
args = parser.parse_args()

def calculate_fizzbuzz(first_in_range,last_in_range):      #dictionary to allocate the correct name to the correct number
    substitutions = {3:'Fizz',5:'Buzz',7:'Fang',11:'Bang'} #the code can be altered to add more name/number combinations
    for i in range(first_in_range,last_in_range):          #if needed
        line = '' #if there is no divisible number, just returns the number in the list
        for n in substitutions.keys():
            if i % n == 0: #if there is a divisible number, return the correct name from the dictionary
                line += substitutions[n]
        print(i,':',line or i) 
        
calculate_fizzbuzz(args.first_in_range,args.last_in_range) #runs the function within the user inputed range