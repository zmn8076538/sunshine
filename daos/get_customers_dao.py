from cfg import cursor

class GetCustomersDao:

    #获取已预约客户
    def get_customers_has_order(self,userId):
        sql = "select insurename,insuregender,phone,ordertime,customer_id from customers where status = 1 and user_id = '{user_id}'"\
            .format(user_id=userId)
        cursor.execute(sql)
        return cursor.fetchall()

    #获取有印象客户
    def get_customers_impressive(self,userId):
        sql = "select insurename,insuregender,phone,notdealreason,customer_id from customers where status = 2 and user_id = '{user_id}'"\
            .format(user_id=userId)
        cursor.execute(sql)
        return cursor.fetchall()

    #获取待确定预约时间客户
    def get_customers_delayordertime(self,userId):
        sql = "select insurename,insuregender,phone,notorderreason,customer_id from customers where status = 3 and user_id = '{user_id}'"\
            .format(user_id=userId)
        cursor.execute(sql)
        return cursor.fetchall()

    #预约上门客户
    def get_customers_visit(self,userId):
        sql = "select insurename,insuregender,phone,address,customer_id from customers where status = 4 and user_id = '{user_id}'" \
            .format(user_id=userId)
        cursor.execute(sql)
        return cursor.fetchall()

    #已出单
    def get_customers_deal(self,userId):
        sql = "select insurename,insuregender,insureidcard,byinsurename,byinsuregender,byidcard,phone,bankcard,address,issuename,safecard,paymentperiod,safeguardperiod,effectiveandexpirationdate,shareperson,customer_id from customers where status = 5 and user_id = '{user_id}'"\
            .format(user_id=userId)
        cursor.execute(sql)
        return cursor.fetchall()

