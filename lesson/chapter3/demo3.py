# 單分支結構
# 範例 : 提款

save=1000                               #存款
withdrawal=int(input('請輸入提款金額'))  #提款金額
if save >= withdrawal :                 # 判斷存款是否充足
    save = save - withdrawal
    print('提款成功,餘額為',save)