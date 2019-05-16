from daos.get_customers_dao import GetCustomersDao

class GetCustomersService:

    get_customers_dao = GetCustomersDao()

    #获取未联系用户
    def get_customers_not_contact(self,userId):
        return self.get_customers_dao.get_customers_not_contact(userId)