def fv(moninv, yeaint, years):
   f_value= 0
   for i in range(years*12):
      f_value+=moninv
      monint= f_value* yeaint/(12*100)
      f_value+= monint
   return f_value
def main():
   import locale as lc
   lc.setlocale(lc.LC_ALL, 'en-ca')
   while True:
      moninv= int(input("Enter monthly investment: "))
      yeaint= float(input("Enter yearly interest rate: "))
      years= int(input("Enter number of years: "))
      future_value_calc = fv(moninv, yeaint, years)

      moninv= lc.currency(moninv,grouping = True)
      future_value_calc= lc.currency(future_value_calc,grouping = True)

      print("\nMonthly investment:\t\t {}".format(moninv))
      print("Yearly interest rate:\t{:>5}".format(yeaint))
      print("Years: \t\t{:>15}".format(years))
      print("Future value: \t\t\t {:<30,.2f}" .format(future_value_calc))
      selection= input("\nContinue? (y/n): ")
      if selection=="y":
         continue
      elif selection=="n":
         break
if __name__ == "__main__":
   main()