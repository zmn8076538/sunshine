from cfg import cursor

class DeleteCustomerDao:

    def delete_customer(self,customer_id):
        sql = "delete from customers where customer_id = '{customer_id}'".format(customer_id=customer_id)
        cursor.execute(sql)