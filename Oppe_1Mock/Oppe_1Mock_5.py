def get_summary(listOfTransactions):
    return [{
        "Cost": sum(
            item['Price'] * item['Qty'] for item in trans['Items']
        ),
        "TID": trans['TID']
    } for trans in listOfTransactions]
