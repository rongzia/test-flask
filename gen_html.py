from all_monthly_link import all_dict
import os
import requests

# 当前目录
current_dir = os.getcwd()
print('current dir :', current_dir)
if not os.path.exists(current_dir + '\\templates') :
    os.mkdir(current_dir + '\\templates')

filename = current_dir + '\\templates' + '\\index.html'
fd = open(filename, mode="w", encoding="utf-8")
fd.write("<!DOCTYPE html>\n"
         "<html lang=\"en\"\n>"
         "<head>\n"
         "    <meta charset=\"UTF-8\">\n"
         "    <title>淘宝日志</title>\n"
         "</head>\n"
         "<body>\n")

for i in all_dict:
    # title = all_dict[i].replace('\\', '').replace('/', '').replace(':', '').replace('*', '')\
    #     .replace('?', '').replace('\"', '').replace('<', '').replace('>', '').replace('|', '')
    title = all_dict[i]
    fd.write("    <a href=\"" + i + "\" target=\"_blank\">" + i.replace("http://mysql.taobao.org/monthly/", "")
             + "&nbsp;&nbsp;&nbsp;&nbsp;" + title + "</a>\n    <br>\n")
fd.write("    </body>\n")
fd.write("</head>")
fd.close()