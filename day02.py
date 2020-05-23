"""变量练习
根据以下格式，提取变量，拼接为一个字符串.
格式： 截至3月24日9时，全国累计报告确诊病例81747例."""
month = 3
day = 24
hour = 9
region = "全国"
definite_count = 81747
message = "截至"+str(month)+"月"+str(day) + "日"+ str(hour) +"时," +region + "全国" +"累计报告确诊病例"+ str(definite_count)+"例."
print(message)
