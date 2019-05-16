from cfg import cursor

class GetCustomersDao:

    #获取未联系客户
    def get_customers_not_contact(self,userId):
        sql = "select customer_name,customer_gender,customer_phonenumber,customer_id from customers where user_id = '{user_id}'"\
            .format(user_id=userId)
        cursor.execute(sql)
        return cursor.fetchall()