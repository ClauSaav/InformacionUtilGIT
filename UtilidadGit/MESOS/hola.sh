!#/bin/bash
contador=0
#HOY=`date`
#while [  $contador -lt 10001 ]; do
#     echo HolaMarathonMesos $contador hora $HOY
#     let contador=contador+1 
#done
STARTTIME=$(date +%s)
#command block that takes time to complete...
#........
ENDTIME=$(date +%s)
while [ $contador -lt 1001 ]; do 
	echo Marathon $contador va $($ENDTIME - $STARTTIME) 
	let contador = contador + 1
done
