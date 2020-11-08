height = input('請輸入身高(cm):')
weight = input('請輸入體重(kg):')
height = float(height)
weight = float(weight)
height = height / 100 # 換算成公尺
BMI = weight / height / height

if BMI < 18.5:
    print('您的BMI為', BMI, '屬體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print('您的BMI為', BMI, '屬正常')
elif BMI >= 24 and BMI < 27:
    print('您的BMI為', BMI, '屬過重')
elif BMI >= 27 and BMI < 30:
    print('您的BMI為', BMI, '屬輕度肥胖')
elif BMI > 30 and BWI < 35:
	print('您的BMI為', BMI, '屬中度肥胖')
else:
	print('您的BMI為', BMI, '屬重度肥胖')