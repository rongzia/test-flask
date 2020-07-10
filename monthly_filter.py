from all_monthly_link import all_dict

keyword = '事务'
for i in all_dict:
    if(keyword in all_dict[i]):
        print(i, end='')
        print('   ' + all_dict[i])