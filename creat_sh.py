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
        'RaceHorses_832x480_30',]
cfgn=['BasketballDrill','BasketballDrillText','BasketballPass',
      'BlowingBubbles','BQMall','BQSquare','FourPeople','Johnny',
      'KristenAndSara','PartyScene','RaceHorses','RaceHorsesC']
i=0
for na in name:
  with open('Run_AI'+na+'.sh','a') as f:
    for qp in [37,32,27,22]:
      f.write('./EncoderApp  -c encoder_intra_vtm.cfg  -c seq/'+
              cfgn[i]+'.cfg  -i seq/'+
              na+'.yuv  -q '+str(qp)+'  -o '+
              na+'_rec_'+str(qp)+'_AI.yuv  -b  '+
              na+'_'+str(qp)+'_AI.bin  > '+na+'_QP'+str(qp)+'_AI.txt ')
      f.write('\r\n')
  with open('Run_RA' + na + '.sh', 'a') as f:
    for qp in [37,32,27,22]:
      f.write('./EncoderApp  -c encoder_randomaccess_vtm.cfg  -c seq/'+
              cfgn[i]+'.cfg  -i seq/'+
              na+'.yuv  -q '+str(qp)+'  -o '+
              na+'_rec_'+str(qp)+'_RA.yuv  -b  '+
              na+'_'+str(qp)+'_RA.bin  > '+na+'_QP'+str(qp)+'_RA.txt v ')
      f.write('\r\n')
  with open('Run_LDB' + na + '.sh', 'a') as f:
    for qp in [37,32,27,22]:
      f.write('./EncoderApp  -c encoder_lowdelay_vtm.cfg  -c seq/'+
              cfgn[i]+'.cfg  -i seq/'+
              na+'.yuv  -q '+str(qp)+'  -o '+
              na+'_rec_'+str(qp)+'_LDB.yuv  -b  '+
              na+'_'+str(qp)+'_LDB.bin  > '+na+'_QP'+str(qp)+'_LDB.txt  ')
      f.write('\r\n')
  with open('Run_LDP' + na + '.sh', 'a') as f:
    for qp in [37,32,27,22]:
      f.write('./EncoderApp  -c encoder_lowdelay_P_vtm.cfg  -c seq/'+
              cfgn[i]+'.cfg  -i seq/'+
              na+'.yuv  -q '+str(qp)+'  -o '+
              na+'_rec_'+str(qp)+'_LDP.yuv  -b  '+
              na+'_'+str(qp)+'_LDP.bin  > '+na+'_QP'+str(qp)+'_LDP.txt ')
      f.write('\r\n')
  i=i+1


