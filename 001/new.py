while True:
    consumption_type = input("vip请输如您的消费类型")
    money = float(input ("请输入您的消费金额"))
    if consumption_type == "vip" :
        if money <=  500:
           print("85折")
        else:
           print("8折")
    else:
        if money >= 800 :
            print ("9折")
        else :
            print ("原价")
    if   input ("先生您还买吗")=="不买了":
        print ("欢迎下次光临")
        break

























