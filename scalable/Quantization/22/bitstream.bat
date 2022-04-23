BitStreamExtractorStatic.exe city_4cif_3L.264 city_r3.264 -sl 3 > scalable_bsextractor_city_r3.txt
BitStreamExtractorStatic.exe city_4cif_3L.264 city_r2.264 -sl 8 > scalable_bsextractor_city_r2.txt
BitStreamExtractorStatic.exe city_4cif_3L.264 city_r1.264 -sl 13 > scalable_bsextractor_city_r1.txt

H264AVCDecoderLibTestStatic city_r3.264 city_r3_dec.y4m>decoded_city_r3.txt
H264AVCDecoderLibTestStatic city_r2.264 city_r2_dec.y4m>decoded_city_r2.txt
H264AVCDecoderLibTestStatic city_r1.264 city_r1_dec.y4m>decoded_city_r1.txt

PSNRStatic 352 288 city_cif.y4m  city_r3_dec.y4m 0 0 city_r3.264 30> PSNR_city_r3.txt
PSNRStatic 704 576 city_4cif.y4m city_r2_dec.y4m 0 0 city_r2.264 60> PSNR_city_r2.txt
PSNRStatic 704 576 city_4cif.y4m  city_r1_dec.y4m 0 0 city_r1.264 60> PSNR_city_r1.txt

BitStreamExtractorStatic.exe soccer_4cif_3L.264 soccer_r3.264 -sl 3 > scalable_bsextractor_soccer_r3.txt
BitStreamExtractorStatic.exe soccer_4cif_3L.264 soccer_r2.264 -sl 8 > scalable_bsextractor_soccer_r2.txt
BitStreamExtractorStatic.exe soccer_4cif_3L.264 soccer_r1.264 -sl 13 > scalable_bsextractor_soccer_r1.txt

H264AVCDecoderLibTestStatic soccer_r3.264 soccer_r3_dec.y4m>decoded_soccer_r3.txt
H264AVCDecoderLibTestStatic soccer_r2.264 soccer_r2_dec.y4m>decoded_soccer_r2.txt
H264AVCDecoderLibTestStatic soccer_r1.264 soccer_r1_dec.y4m>decoded_soccer_r1.txt

PSNRStatic 352 288 soccer_cif.y4m  soccer_r3_dec.y4m 0 0 soccer_r3.264 30> PSNR_soccer_r3.txt
PSNRStatic 704 576  soccer_4cif.y4m soccer_r2_dec.y4m 0 0 soccer_r2.264 60> PSNR_soccer_r2.txt
PSNRStatic 704 576  soccer_4cif.y4m  soccer_r1_dec.y4m 0 0 soccer_r1.264 60> PSNR_soccer_r1.txt

pause
