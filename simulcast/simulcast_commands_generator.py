# Simulcast case
simulcast_tup = ('singlelayer_soccer_704_576_60','singlelayer_soccer_352_288_30',
                 'singlelayer_city_704_576_60', 'singlelayer_city_352_288_30')

#basisqP = [20,22,25,27,30,32,35,37,40]
# Number of frames to encode
#seqframes = (50,80,100,120,150,200,250,300,450,600)
#indframe = 0
#, open ('')
#f = open('commands_simulcast.txt','w')

with open('commands_simulcast.txt','w') as commandfile, open('simulcast.bat','w') as simulcastfile:
    #for indframe in seqframes:
    for i,val in enumerate(simulcast_tup):
#i = int(input('Introduce the stream: 0,1 soccer in 4cif,cif and 2,3 city in 4cif,cif: '))
        strippedsimulcast = val.rsplit('_')
        #print(strippedsimulcast)

        inputfile = simulcast_tup[i]  +'.y4m'
        outputfile = simulcast_tup[i]+'_coded.264'
        reconstructedfile = simulcast_tup[i]+'_rec.y4m' # or yuv
        sourceWidth = strippedsimulcast[2]        # input  frame width
        sourceHeight = strippedsimulcast[3]        # input  frame height
        frameRate =  strippedsimulcast[4]       # frame rate [Hz]
        decoded = simulcast_tup[i] +'_decoded.y4m'
        # Write the cfg file

        # Write the file with the commands needed
        encoder_name = 'encoded_'+ val  + '.txt' # + '>' + encoder_name
        decoder_name = 'decoded_'+ val + '.txt' # + '>' + decoder_name
        psnr_name = 'psnr_' + val + '.txt'
        encoder_output = 'H264AVCEncoderLibTestStatic -pf ' +  simulcast_tup[i] + '.cfg' + '>' + encoder_name
        decoder_output = 'H264AVCDecoderLibTestStatic'+ ' ' + outputfile  + ' ' + decoded  + '>' + decoder_name # or yuv
        psnr_output = 'PSNRStatic' +  ' ' + sourceWidth +  ' ' +  sourceHeight + ' ' +  inputfile + ' '  + decoded + ' ' +  '0' + ' '+ '0' + ' ' + outputfile + ' ' + frameRate + '>' + psnr_name 
        
        commandfile.write (f'The video file is {inputfile} with framerate {frameRate}')
        commandfile.write('\n')
        commandfile.write(f'For 100 frames to encode, the following are the commands to use:')
        commandfile.write('\n')
        commandfile.write (encoder_output)
        
        commandfile.write('\n')
        commandfile.write(decoder_output)
        commandfile.write('\n')
        commandfile.write(psnr_output)

        commandfile.write('\n')
        commandfile.write ('------------------------------')
        commandfile.write('\n')
        commandfile.write ('------------------------------')
        commandfile.write('\n')
        commandfile.write ('------------------------------')
        commandfile.write('\n')
        commandfile.write ('------------------------------')
        commandfile.write('\n')

        simulcastfile.write(encoder_output)
        simulcastfile.write('\n')
        simulcastfile.write(decoder_output)
        simulcastfile.write('\n')
        simulcastfile.write(psnr_output)
        simulcastfile.write('\n')
        

        #print(encoder_output)
        #print(decoder_output)
        #print(psnr_output)

f = open('simulcast.bat','a')
f.write('pause')
f.close

# H264AVCDecoderLibTestStatic SOCCER_704_576_600_60_coded.264 SOCCER_704_576_600_60_decoded.yuv
