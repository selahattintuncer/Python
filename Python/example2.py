job = input("Lütfen işinizi yazınız")
age = int(input("lütfen yaşınızı yazınız"))
numb_child = int(input("Lütfen çocuk sayısını giriniz"))

job_check = job == "memur"
age_check = age <= 50
numb_child_check = numb_child < 3

if (job_check and age_check and numb_child_check):
    print("Kredi alabilirisniz")
else:
    print("Üzgünüz kredi alamazsınız")


print("selo")
