echo "Scalable Case"
echo "Scalable 3 layers city"
H264AVCEncoderLibTestStatic.exe -pf scalable_3L_city_4cif.cfg> scalable_city.txt
echo "Scalable 3 layers soccer"
H264AVCEncoderLibTestStatic.exe -pf scalable_3L_soccer_4cif.cfg> scalable_soccer.txt
echo "Showing layers city"
BitStreamExtractorStatic.exe city_4cif_3L.264> scalable_city_bsextractor.txt
echo "Showing layers soccer"
BitStreamExtractorStatic.exe soccer_4cif_3L.264> scalable_soccer_bsextractors.txt
pause