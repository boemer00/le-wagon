def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    results = db.execute("""
                        SELECT Orders.OrderID, Customers.ContactName, Employees.FirstName
                        FROM Orders
                        JOIN Customers ON Customers.CustomerID = Orders.CustomerID
                        JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
                        """)
    return results.fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    '''
    results = db.execute("""
                         SELECT Customers.ContactName, SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS total_amount 
                         FROM OrderDetails
                         JOIN Orders ON Orders.OrderID = OrderDetails.OrderID
                         JOIN Customers ON Customers.CustomerID = Orders.CustomerID
                         GROUP BY Customers.ContactName
                         ORDER BY total_amount ASC;
                         """)
    return results.fetchall()

def best_employee(db):
    '''return the first and last name of the best employee (the one
    who sells the most in terms of amount of money'''
    query = """SELECT Employees.FirstName, Employees.LastName,
                      SUM(UnitPrice * Quantity) as total_sales
               FROM Orders
               JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
               JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
               GROUP BY Employees.LastName
               ORDER BY total_sales DESC
               LIMIT 1;
               """
    db.execute(query)
    results = db.fetchall()
    return results

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = """SELECT Customers.ContactName, COUNT(Orders.OrderID) AS total_orders
               FROM Customers
               LEFT JOIN Orders ON Orders.CustomerID = Customers.CustomerID
               GROUP BY Customers.ContactName
               ORDER BY total_orders ASC;
               """
    db.execute(query)
    results = db.fetchall()
    return results
