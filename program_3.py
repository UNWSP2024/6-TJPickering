#Programmer: Timothy Pickering
#Date: 2/27/2025
#Title: Tax Calc for Sales

def calculateTaxes(monthlySales):
#Tax rates
    stateTaxRate = 0.05
    countyTaxRate = 0.025

#Calculate taxes
    stateTax = monthlySales * stateTaxRate
    countyTax = monthlySales * countyTaxRate
    totalTax = stateTax + countyTax

#Return values
    return countyTax, stateTax, totalTax

#Mainline
if __name__ == "__main__":

#Get user input
    monthlySales = float(input("Enter the total sales for the month: $"))

#Calculate taxes by calling the function
    countyTax, stateTax, totalTax = calculateTaxes(monthlySales)

#Display results
    print(f"State Sales Tax:  ${stateTax:.2f}")
    print(f"County Sales Tax: ${countyTax:.2f}")
    print(f"Total Sales Tax:  ${totalTax:.2f}")
