from cfg import cursor

class AddCustomerDao:

    def add_customer(self,userid,name,gender,phonenumber,product,payment,paymentyear,safeguard,detail,idcard,bankcard,safecard):
        sql = "insert into customers" \
              "(user_id,customer_name,customer_gender,customer_phonenumber,customer_product,customer_payment,customer_paymentyear,customer_safeguard,customer_detail,customer_idcard,customer_bankcard,customer_safecard) " \
              "values('{userid}','{name}','{gender}','{phonenumber}','{product}','{payment}','{paymentyear}','{safeguard}','{detail}','{idcard}','{bankcard}','{safecard}')"\
            .format(userid=userid,name=name,gender=gender,phonenumber=phonenumber,product=product,payment=payment,paymentyear=paymentyear,safeguard=safeguard,detail=detail,idcard=idcard,bankcard=bankcard,safecard=safecard)

        return cursor.execute(sql) == 1