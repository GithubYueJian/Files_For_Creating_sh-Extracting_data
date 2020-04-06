#一次性把所有配置的序列数据结果提取出来
#格式要求：**_QP32_AI.txt

import xlwt
#所有序列数据主名称
name = ['BasketballDrill_832x480_50',
        'BasketballDrillText_832x480_50',
        'BasketballPass_416x240_50',
        'BlowingBubbles_416x240_50',
        'BQMall_832x480_60',
        'BQSquare_416x240_60',
        'FourPeople_1280x720_60',
        'Johnny_1280x720_60',
        'KristenAndSara_1280x720_60',
        'PartyScene_832x480_50',
        'RaceHorses_416x240_30',
        'RaceHorses_832x480_30',
        'SlideShow_1280x720_20']
#创建表，第一次循环（编码模式）,第二次循环（qp）
f = xlwt.Workbook()
for mode in ['AI','RA','LDB','LDP']:
  sheet = f.add_sheet(mode, cell_overwrite_ok=True)
  j = 1
  i = 0
  for name_seq in name:
    sheet.write(j, 1, name_seq)
    for i in range(0,4):
      sheet.write(j+i, 2, 22+5*i)
      with open(name_seq+'_QP'+str(22+5*i)+'_'+mode+'.txt') as ftxt:
        content = ftxt.read().splitlines()
        data1=content[-4].split( )
        data2=content[-1].split( )
        data = data1[2:]
        data.append(data2[5])
        k=3
        for target in data:
           sheet.write(j+i,k,target)
           k=k+1
f.save('data.xls')
