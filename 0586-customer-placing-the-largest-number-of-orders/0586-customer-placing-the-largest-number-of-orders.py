import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Count orders per customer
    counts = orders['customer_number'].value_counts()
    
    # Find the maximum count
    max_count = counts.max()
    
    # Select customer(s) with that maximum
    top_customers = counts[counts == max_count]
    
    # Return as DataFrame
    top_customers =top_customers.reset_index()
    print(top_customers)
    return top_customers['customer_number'].to_frame()
