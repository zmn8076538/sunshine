from daos.add_customer_dao import AddCustomerDao

class AddCustomerService:

    add_cutomer_dao = AddCustomerDao()

    def add_customer(self,user_id,customer_name,customer_gender,customer_phonenumber):
        return self.add_cutomer_dao.add_customer(user_id,customer_name,customer_gender,customer_phonenumber)
