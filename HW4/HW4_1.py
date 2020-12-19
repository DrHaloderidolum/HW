from sys import argv
script_name, output_in_hours, rate, premium = argv
output_in_hours = float(output_in_hours)
rate = float(rate)
premium = float(premium)
salary = ((output_in_hours*rate)+premium)
print(f"Output_in_hours is: {output_in_hours}")
print(f"Rate is: {rate}")
print(f"Premium is: {premium}")
print(f"Salary is: {salary}")
