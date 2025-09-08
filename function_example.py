def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    
    print(f"Bill: ${bill_amount:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    
    return total