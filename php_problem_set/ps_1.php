<?php
date_default_timezone_set('Europe/Istanbul');
$time=date('H');
if("06"<= $time && $time<"10"){echo "Günaydın";}
else if("10"<= $time && $time<"17"){echo "İyi günler.";}
else if("17"<= $time && $time<"20"){echo "İyi aksamlar.";}
else if("20"<= $time && $time<"00"){echo "İyi iyi geceler.";}
else if("00"<= $time && $time<"06"){echo "Esenlikler dilerim.";}
else{echo "hata";}
?>