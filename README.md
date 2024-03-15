# pension_buyback_analysis

## DISCLAIMER

The logic in this code is not intended as any kind of advice. Please use at your own risk.
Consult a professional before undertaking major financial decisions.

## Use Case

This code can be useful in a situation when an employee is given an offer to buy back his/her new pension with funds from an existing pension that is now closed, and needs to decide if to accept the offer or reject it. When rejecting the offer, existing defined benfit funds will need to be invested somewhere else. It is my take on evaluating an offer systematically and quantitatively.  

An employee's journey to retirement income is normally divided into two stages: **pre-retirement** and **retirement**. In the analysis, the code takes into account the cost of your contributions and your employer's contribuitions in addition to the cost of the buyback amount during the pre-retirement stage. Then, during retirement stage, the analysis uses an annuity formula to evaluate pension income.

One of the key assumptions that an employee/user needs to make, is to estimate the expected pension growth rate during each of the stages. This is not obvious at all and no one knows the answer with certainty. You are on your own to do your research and make an estimate.

The code uses the concept of [Time Value of Money](https://www.investopedia.com/terms/t/timevalueofmoney.asp) to compound and discount.

The purpose of this code is to estimate:

1. Pension Value at 65
2. Pension Annuity Value at 65
3. Difference between 1. and 2., which may suggest that buyback may be OVERVALUED/UNDERVALUED  

## User Interface

Pension Buyback Analysis app is designed as a command-line application (or console application) which is to be used from a text interface, such as a shell.
The software has been tested to runs in Windows terminal. There is currently no web version.

## Expected user input

Since each person's situation is unique, calculations are based on users input. User will need to estimate **Expected death age**, projected annual investment rates of return for **Pre-retirement stage (till 65)** and **Retirement stage (after 65)**. In addition, user will need to enter personal information plus information from pension buyback offer letter (**Buyback amount** and **Guaranteed annual pension**).

## Software Requirements

You will need to install and run this code on your computer and OS. A Google search will lead you to guides such as [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) but I  have not checked it for correctness or completeness.
