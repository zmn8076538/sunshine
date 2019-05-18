from cfg import cursor

class AddCustomerDao:

    def add_customer(self,userId,insurename,insuregender,insureidcard,byinsurename,byinsuregender,byidcard,relationship,phone,address,bankcard,issuename,safecard,paymentperiod,safeguardperiod,effectiveandexpirationdate,ordertime,notdealreason,notorderreason,shareperson,detail,status):
        sql = "insert into customers" \
              "(user_id,insurename,insuregender,insureidcard,byinsurename,byinsuregender,byidcard,relationship,phone,address,bankcard,issuename,safecard,paymentperiod,safeguardperiod,effectiveandexpirationdate,ordertime,notdealreason,notorderreason,shareperson,detail,status) " \
              "values('{userId}','{insurename}','{insuregender}','{insureidcard}','{byinsurename}','{byinsuregender}','{byidcard}','{relationship}','{phone}','{address}','{bankcard}','{issuename}','{safecard}','{paymentperiod}','{safeguardperiod}','{effectiveandexpirationdate}','{ordertime}','{notdealreason}','{notorderreason}','{shareperson}','{detail}','{status}')"\
            .format(userId=userId,insurename=insurename,insuregender=insuregender,insureidcard=insureidcard,byinsurename=byinsurename,byinsuregender=byinsuregender,byidcard=byidcard,relationship=relationship,phone=phone,address=address,bankcard=bankcard,issuename=issuename,safecard=safecard,paymentperiod=paymentperiod,safeguardperiod=safeguardperiod,effectiveandexpirationdate=effectiveandexpirationdate,ordertime=ordertime,notdealreason=notdealreason,notorderreason=notorderreason,shareperson=shareperson,detail=detail,status=status)

        return cursor.execute(sql) == 1