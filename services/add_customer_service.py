from daos.add_customer_dao import AddCustomerDao

class AddCustomerService:

    add_cutomer_dao = AddCustomerDao()

    def add_customer(self,user_id,customer_name,customer_gender,customer_phonenumber,customer_product,customer_payment,customer_paymentyear,customer_safeguard,customer_detail,customer_idcard,customer_bankcard,customer_safecard):
        return self.add_cutomer_dao.add_customer(user_id,customer_name,customer_gender,customer_phonenumber,customer_product,customer_payment,customer_paymentyear,customer_safeguard,customer_detail,customer_idcard,customer_bankcard,customer_safecard)
