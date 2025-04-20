def calculate_due_amount(total_bill, amount_paid):
    if amount_paid >= total_bill:
        print("No due amount. The customer has paid in full")
        return 0.0
    else:
        due_amount = total_bill - amount_paid
        print(f"The due amount ₹{due_amount:.2f} ")
        return due_amount
    

print("Customer Bill Payment")
total_bill = float(input("Enter the total bill amount: ₹"))
amount_paid = float(input("Enter the amount paid by the customer: ₹"))
calculate_due_amount(total_bill, amount_paid)