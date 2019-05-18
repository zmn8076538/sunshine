from daos.add_customer_dao import AddCustomerDao

class AddCustomerService:

    add_cutomer_dao = AddCustomerDao()

    def add_customer(self,userId,insurename,insuregender,insureidcard,byinsurename,byinsuregender,byidcard,relationship,phone,address,bankcard,issuename,safecard,paymentperiod,safeguardperiod,effectiveandexpirationdate,ordertime,notdealreason,notorderreason,shareperson,detail,status):
        return self.add_cutomer_dao.add_customer(userId,insurename,insuregender,insureidcard,byinsurename,byinsuregender,byidcard,relationship,phone,address,bankcard,issuename,safecard,paymentperiod,safeguardperiod,effectiveandexpirationdate,ordertime,notdealreason,notorderreason,shareperson,detail,status)
