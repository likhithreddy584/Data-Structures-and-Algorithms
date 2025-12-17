def transaction_amounts(amounts):
    for amount in amounts:
        if amount < 0 :
            continue
        elif amount == 9999 :
            print("stop signal received ")
            break 
        else :
            print("processing :" ,amount )