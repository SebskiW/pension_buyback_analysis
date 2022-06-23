import numpy as np
import numpy_financial as npf
from  datetime import date 

from os import system, name
#############################################################################################################
### DISCLAIMER - The logic in this code is not intended as any kind of advice. Please use at your own risk. 
################ Consult a professional before undertaking major financial decisions. 
#############################################################################################################
#The purpose of this code is to estimate:
# 1. Pension Value at 65
# 2. Pension Annuity Value at 65
# 3. Difference between 1. and 2., which may suggest that buyback may be OVERVALUED/UNDERVALUED  
# 
# User will need to estimate:
# 4. Expected death age

# User will need to estimate projected annual investment rates of return for:
# 5. Pre-retirement stage (till 65)
# 6. Retirement stage (after 65)  
# 
# User will need to enter personal information plus information from pension buyback offer letter:
# 7. Buyback amount
# 8. Guaranteed annual pension
# 
#  

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
        _ = system('clear')

def main():
    clear()
    #fictitious default values. feel free to replace with your situation 
    CURRENT_YMPE=61600       #defined by government annualy. 2022 YMPE
    TIER1_CONTRIB_RATE=0.074 #defined by pension contribution rate below YMPE
    TIER2_CONTRIB_RATE=0.105 #defined by pension contribution rate above YMPE 
    FULL_BUYBACK_AMOUNT="100000.01" #fictitious amount provided in pension buyback package 
    ANNUAL_PENSION="30000.01" #fictitious amount provided in pension buyback package
    CURRENT_AGE="50"
    CURRENT_SALARY="100000"
    EST_DEATH_AGE="90"

    #Accumumulation stage default assumptions
    PENSION_GROWTH_RATE = 5.0 #assume a conservative rate in %
    
    #Distribution stage default assumptions
    ANNUITY_DISCOUNT_RATE = 5.0 #assume a conservative rate in %
    #ANNUITY_DISCOUNT_RATE_TEXT="assumed annuity discount rate"

    #Prompt for info about annunitant
    age=int(input("Age: ") or CURRENT_AGE)
    print(age)
    current_salary=float(input("Current Salary: ") or CURRENT_SALARY)
    print(current_salary)
    est_death_age=int(input("Estimate Death Age: ") or EST_DEATH_AGE)
    print(est_death_age)
    pension_length = est_death_age-65 

    #Prompt for pension offer details
    full_buyback_amount=float(input("Pension full buyback amount: ") or FULL_BUYBACK_AMOUNT)
    print(full_buyback_amount)
    guaranteed_lifetime_annual_pension=float(input("Annual pension: ") or ANNUAL_PENSION)
    print(guaranteed_lifetime_annual_pension)

    years_till_retirement=65-age

   
    #Prompt for internal pension assumptions
    pension_growth_rate=float(input("[PRE-RETIREMENT STAGE] Expected pension growth rate in %: ") or PENSION_GROWTH_RATE)
    print(pension_growth_rate)
    annuity_discount_rate=float(input("[RETIREMENT STAGE] Expected annuity discount rate in %: ") or ANNUITY_DISCOUNT_RATE)
    print(annuity_discount_rate)
    
    
    #OPTION_HEADINGS
    #RET_OPTION_TEXT="retirement option"
    #RET_DATE_TEXT="retirement date"
    #RET_ANN_PENS65_TEXT="pension at 65"

    #my headings and text
    #ANNUITY_DISCOUNT_RATE_TEXT="assumed annuity discount rate"

    #Pension Offer Option 1.1 - Retirement option=Age 65
    pension_option1={} #empty dict
    pension_option1["ret_option"]="Age 65"
    pension_option1["ret_year"]= date.today().year+years_till_retirement
    pension_option1["ann_pens65"]=guaranteed_lifetime_annual_pension

    print ("Assumptions:")
    print("Pension Buyback OFFER Option 1.1 - Retirement option=Age 65")
    #print all text labels, one per line
    for key, value in pension_option1.items():
        print(key, value)

        
    #estimate all my contributions (cost)
    tier1_contrib=0
    tier2_contrib=0
    my_annual_contrib=0
    if current_salary<=CURRENT_YMPE:
        tier1_contrib=current_salary*TIER1_CONTRIB_RATE
    elif current_salary>CURRENT_YMPE:
        tier1_contrib=CURRENT_YMPE*TIER1_CONTRIB_RATE
        tier2_contrib=(current_salary-CURRENT_YMPE)*TIER2_CONTRIB_RATE

    my_annual_contrib=tier1_contrib+tier2_contrib

    print("\n"+"****Compound contributions from TODAY to value at 65***")
    print("Assumptions: Salary remains constant till 65")
    print("My annual contribs: "+"${:,.2f}".format(my_annual_contrib))

    #estimate all my employer contributions
    employer_annual_contrib=my_annual_contrib

    #from buyback
    fv1=-npf.fv(pension_growth_rate/100,years_till_retirement,0,full_buyback_amount)

    #from my contribs
    print("Future value of all contributions at age 65")
    fv2=-npf.fv(pension_growth_rate/100,years_till_retirement,my_annual_contrib,0)
    #from employer contribs
    fv3=-npf.fv(pension_growth_rate/100,years_till_retirement,employer_annual_contrib,0)

    fv1_currency = "${:,.2f}".format(fv1)
    print("Future value of my buyback: "+fv1_currency)

    fv2_currency = "${:,.2f}".format(fv2)
    print("Future value of my contribs: "+fv2_currency)

    fv3_currency = "${:,.2f}".format(fv3)
    print("Future value of employer contribs: "+ fv3_currency)

    fv_total=fv1+fv2+fv3
    fv_total_currency="${:,.2f}".format(fv_total)
    print("Total Pension Value at 65: "+fv_total_currency)

#calculate pension value at 65 of all pension annuity payments
    print("\n"+"****Discount pension annuity payments to value at 65***")
    print("Assumption 1: Annuity payment are NOT INDEXED to cost of living.")
    print("Assumption 2: Survivor benefit is excluded.")
    pv65=0.00
    rate=annuity_discount_rate/100
    nper=pension_length #years from 65 till est death
    pmt=-pension_option1["ann_pens65"]
    pv65=npf.pv(rate, nper, pmt )
    currency = "${:,.2f}".format(pv65)

    print("Pension Annuity Value at 65: "+ currency)
    benefit_cost=pv65-fv_total
    
    print("\n")
    print("Benefit - Cost difference: "+"${:,.2f}".format(benefit_cost))
    if benefit_cost <0:
        print("Your pension buyback may be OVERVALUED.")
    else:
        print("Your pension buyback may be UNDERVALUED.")    
    print("\n")

if __name__ == "__main__":
    main()