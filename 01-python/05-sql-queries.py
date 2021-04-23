def query_orders(db):
    # return a list of orders displaying each column
    results = db.execute("""
                         SELECT *
                         FROM Orders
                         ORDER BY OrderID ASC;
                         """)
    return results.fetchall()

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate
    # between date_from and date_to
    results = db.execute("""
                         SELECT *
                         FROM Orders
                         WHERE OrderDate > ?
                         AND OrderDate <= ?
                         ORDER BY OrderDate ASC;
                         """, (date_from, date_to))
    results = results.fetchall()
    final_list = []
    for order in results:
        final_list.append(order)
    return final_list

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    results = db.execute("""
                         SELECT *, JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) as timedelta
                         FROM Orders
                         ORDER BY timedelta ASC;
                         """)
    results = results.fetchall()
    return results
