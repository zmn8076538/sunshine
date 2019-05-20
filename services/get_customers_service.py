from daos.get_customers_dao import GetCustomersDao

class GetCustomersService:

    get_customers_dao = GetCustomersDao()

    #获取未联系用户
    def get_customers_has_order(self,userId):
        return self.get_customers_dao.get_customers_has_order(userId)

    #有印象
    def get_customers_impressive(self,userId):
        return self.get_customers_dao.get_customers_impressive(userId)

    #待确定预约时间
    def get_customers_delayordertime(self,userId):
        return self.get_customers_dao.get_customers_delayordertime(userId)

    #预约上门
    def get_customers_visit(self,userId):
        return self.get_customers_dao.get_customers_visit(userId)

    #已出单
    def get_customers_deal(self,userId):
        return self.get_customers_dao.get_customers_deal(userId)