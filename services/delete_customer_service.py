from daos.delete_customer_dao import DeleteCustomerDao

class DeleteCustomerService:

    delete_customer_dao = DeleteCustomerDao()

    def delete_customer(self,customer_id):
        self.delete_customer_dao.delete_customer(customer_id)