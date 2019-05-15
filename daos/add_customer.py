from cfg import cursor

class AddCustomer:

    def add_customer(self,user_id,customer_name,customer_gender,customer_phonenumber,customer_product,customer_payment,customer_paymentyear,customer_safeguard,customer_detail,customer_idcard,customer_bankcard,customer_safecard):
        sql = "insert into customers" \
              "(user_id,customer_name,customer_gender,customer_phonenumber,customer_product,customer_payment,customer_paymentyear,customer_safeguard,customer_detail,customer_idcard,customer_bankcard,customer_safecard) " \
              "values({user_id},'{customer_name}','{customer_gender}',{customer_phonenumber},'{customer_product}','{customer_payment}','{customer_paymentyear}','{customer_safeguard}','{customer_detail}','{customer_idcard}','{customer_bankcard}','{customer_safecard}')"\
            .format(user_id=user_id,customer_name=customer_name,customer_gender=customer_gender,customer_phonenumber=customer_phonenumber,customer_product=customer_product,customer_payment=customer_payment,customer_paymentyear=customer_paymentyear,customer_safeguard=customer_safeguard,customer_detail=customer_detail,customer_idcard=customer_idcard,customer_bankcard=customer_bankcard,customer_safecard=customer_safecard)

        return cursor.execute(sql) == 1