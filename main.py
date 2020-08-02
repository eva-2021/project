from Classes import InventoryClass, InventoryListClass, SiparisListClass

import pandas as pd
from pandas import DataFrame
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")

while True:
    number=int(input("\nINVENTORY CONTROL SYSTEM\n 1.Inventory\n 2.Order\n 3.Labor\n 0.Exit\n"))
    if number==0:
        break

    if number==1:
        while True:
            number1=int(input("1. View inventory\n2. Update inventory\n3. Product information\n0. Go back\n"))
            if number1==1:
                for obj in InventoryListClass.getinstances():
                    print("Product Code:", obj.inventory_code, "    Product Name:", obj.inventory_name, "    Amount:",
                          obj.inventory_amount, obj.inventory_unit, "    Location:", obj.inventory_location)

            if number1==2:
                print(":(")

            if number1==3:
                print(":(")
            else:
                break

    if number==2:
        while True:

            number2=int(input("1. Current orders\n2. New order\n3. Completed orders\n0. Go back\n"))

            df5 = pd.read_excel('OrderCurrent.xlsx')
            OrderCurrent_OrderNo = df5['OrderCurrent_OrderNo'].tolist()
            OrderCurrent_ProductCode = df5["OrderCurrent_ProductCode"].tolist()
            OrderCurrent_ProductCode2 = df5["OrderCurrent_ProductCode"].tolist()
            OrderCurrent_ProductName = df5["OrderCurrent_ProductName"].tolist()
            OrderCurrent_Amount = df5["OrderCurrent_Amount"].tolist()
            OrderCurrent_Date = df5["OrderCurrent_Date"].tolist()





            if number2==1:
                for obj in SiparisListClass.getinstances():
                    print("Order No:", obj.OrderCurrent_OrderNo, "    Product Code:", obj.OrderCurrent_ProductCode,
                          "    Product name:",
                          obj.OrderCurrent_ProductName, "    Amount:", obj.OrderCurrent_Amount, "    Date:",
                          obj.OrderCurrent_Date)
            if number2==2:
                df = pd.read_excel('OrderNew.xlsx')

                OrderNew_OrderNo= df['OrderNew_OrderNo'].tolist()
                OrderNew_ProductCode=df["OrderNew_ProductCode"].tolist()
                OrderNew_ProductName= df["OrderNew_ProductName"].tolist()
                OrderNew_Amount= df["OrderNew_Amount"].tolist()
                OrderNew_Date= df["OrderNew_Date"].tolist()

                a = int(input("Order no: "))
                b = int(input("Product amount: "))

                i = 0
                while i < b:
                    OrderNew_OrderNo.append(a)
                    OrderNew_Date.append(d1)
                    OrderCurrent_Date.append(d1)
                    c=int(input("Product code: "))
                    OrderNew_ProductCode.append(c)
                    OrderCurrent_ProductCode.append(c)
                    d = str(input('Product name: '))
                    OrderNew_ProductName.append(d)
                    OrderCurrent_ProductName.append(d)
                    e = int(input('Amount: '))
                    OrderNew_Amount.append(e)
                    OrderCurrent_Amount.append(e)
                    print("Successful.")
                    i += 1
                    print(OrderCurrent_ProductName)
                    p = zip(OrderNew_OrderNo, OrderNew_ProductCode, OrderNew_ProductName,
                           OrderNew_Amount , OrderNew_Date)
                    df2 = DataFrame(p)
                    df2.columns = ["OrderNew_OrderNo","OrderNew_ProductCode", "OrderNew_ProductName",
                                   "OrderNew_Amount", "OrderNew_Date"]

                    writer = pd.ExcelWriter('OrderNew.xlsx', engine='xlsxwriter')
                    df2.to_excel(writer, sheet_name='Sheet1')

                    p2=zip(OrderCurrent_OrderNo, OrderCurrent_ProductCode, OrderCurrent_ProductName,
                           OrderCurrent_Amount, OrderCurrent_Date)
                    df5=DataFrame(p2)
                    df5.columns=["OrderCurrent_OrderNo","OrderCurrent_ProductCode","OrderCurrent_ProductName",
                                 "OrderCurrent_Amount","OrderCurrent_Date"]

                    writer2=pd.ExcelWriter("OrderCurrent.xlsx", engine="xlsxwriter")
                    df5.to_excel(writer, sheet_name="Sheet2")
                    writer.save()
                    writer2.save()


                    break
            if number2==3:
                print("sad face")
                break
            else:
                break
    if number==3:
    #is dosyasını ac ve tarihi oku
        df = pd.read_excel('worker.xlsx')

        worker_name=df['Name'].tolist()
        Job=df["Job"].tolist()
        Amount=df["Amount"].tolist()
        Date=df["Date"].tolist()

        temp_worker_name=(str(input("Worker Name: ")))
        temp_Job=(str(input("Job: ")))
        temp_Amount=(int(input("Amount: ")))

        if temp_Job=="cc":
            boya1.add(99999999)
            boya2.add(88888888)
            boya1.update()
            boya2.update()
        else:
            print("nooo")
        #Excele aktar
        worker_name.append(temp_worker_name)
        Job.append(temp_Job)
        Amount.append(temp_Amount)
        Date.append(d1)

        p = zip(worker_name, Job, Amount,Date)
        df2 = DataFrame(p)
        df2.columns = ["Name", "Job", "Amount","Date"]

        writer = pd.ExcelWriter('worker.xlsx', engine='xlsxwriter')
        df2.to_excel(writer, sheet_name='Sheet1')

        writer.save()

