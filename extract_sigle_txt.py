#一次性把所有配置的序列数据结果提取出来
#格式要求：**_QP32_AI.txt
dir =r'C:\Users\YueJian\Desktop\hm-test-linux\hm-benchmark\RUN\txt\\'
import xlwt
#所有序列数据主名称
name = ['BasketballPass_416x240_50']
#创建表，第一次循环（编码模式）,第二次循环（qp）
f = xlwt.Workbook()
for mode in ['AI']:
  sheet = f.add_sheet(mode, cell_overwrite_ok=True)
  j = 1
  i = 0
  for name_seq in name:
    sheet.write(j, 1, name_seq)
    for i in range(0,4):
      sheet.write(j+i, 2, 22+5*i)
      with open(dir+name_seq+'_QP'+str(22+5*i)+'_'+mode+'.txt') as ftxt:
      #with open(r'C:\Users\YueJian\Desktop\YUV\BasketballPass_416x240_50.txt') as ftxt:
        content = ftxt.read().splitlines()
        data1=content[-21].split( )
        data2=content[-1].split( )
        print(data1)
        data = data1[2:]
        data.append(data2[2])
        for d in data:
          d=float(d)
        k=3
        for target in data:
           sheet.write(j+i,k,target)
           k=k+1
f.save('data8.xls')
