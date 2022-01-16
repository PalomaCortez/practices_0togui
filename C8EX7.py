## Cap 8 - GUI
# EX7 - Loan Calculator with GUI

from tkinter import *


class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")

        Label(window, text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(window, text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(window, text="Total Payment").grid(row=5, column=1, sticky=W)

        self.annual_interest_rate_var = StringVar()
        Entry(window, textvariable=self.annual_interest_rate_var,
              justify=RIGHT).grid(row=1, column=2)
        self.number_years_var = StringVar()
        Entry(window, textvariable=self.number_years_var,
              justify=RIGHT).grid(row=2, column=2)
        self.loan_amount_var = StringVar()
        Entry(window, textvariable=self.loan_amount_var,
              justify=RIGHT).grid(row=3, column=2)

        self.monthly_payment_var = StringVar()
        lbl_monthly_payment = Label(window, textvariable=
        self.monthly_payment_var, justify=RIGHT).grid(row=4, column=2,
                                                      sticky=E)
        self.total_payment_var = StringVar()
        lbl_total_payment = Label(window, textvariable=
        self.total_payment_var, justify=RIGHT).grid(row=5, column=2,
                                                      sticky=E)
        btComputePayment = Button(window, text="Compute Payment",
                                    command=self.compute_payment).grid(
            row=6, column=2, sticky=E)

        window.mainloop()


    def compute_payment(self):
        monthly_payment = self.get_monthly_payment(
            float(self.loan_amount_var.get()),
            float(self.annual_interest_rate_var.get())/1200,
            int(self.number_years_var.get()))
        self.monthly_payment_var.set(format(monthly_payment, "10.2f"))
        total_payment = float(self.monthly_payment_var.get()) * 12 \
                        * int(self.number_years_var.get())
        self.total_payment_var.set(format(total_payment, "10.2f"))

    def get_monthly_payment(self,
                            loan_amount, monthly_interest_rate, number_years):
        monthly_payment = loan_amount * monthly_interest_rate / (1
                                                                 - 1 / (1 + monthly_interest_rate) ** (number_years * 12))
        return monthly_payment;


LoanCalculator()
