name = ['BasketballPass_416x240_50']
cfgn=['BasketballPass']
#HM TAppEncoderStatic encoder_intra_main.cfg
#VTM EncoderApp  encoder_intra_vtm.cfg
#

for na in name:
  with open('Run_AI_'+na+'.sh','w') as f:
    for qp in [37,32,27,22]:
      f.write('./TAppEncoderStatic  -c ../code_cfg/encoder_intra_main.cfg  -c ../seq_cfg/'+
              cfgn[0]+'.cfg  -i ../seq/'+
              na+'.yuv  -q '+str(qp)+'  -o '+'../rec/'+
              na+'_rec_'+str(qp)+'_AI.yuv  -b  '+'../bin/'+
              na+'_'+str(qp)+'_AI.bin  > '+'../txt/'+na+'_QP'+str(qp)+'_AI.txt ')
      f.write('\r\n')