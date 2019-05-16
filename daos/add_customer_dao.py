from cfg import cursor

class AddCustomerDao:

    def add_customer(self,userid,name,gender,phonenumber):
        sql = "insert into customers" \
              "(user_id,customer_name,customer_gender,customer_phonenumber) " \
              "values('{userid}','{name}','{gender}','{phonenumber}')"\
            .format(userid=userid,name=name,gender=gender,phonenumber=phonenumber)

        return cursor.execute(sql) == 1