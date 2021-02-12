<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
 .header {
  padding: 60px;
  text-align: center;
  background: #1abc9c;
  color: white;
  font-size: 30px;
 
}
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
<body>
<div class="header">
  <h1>Mükemmel Sayıyı Buluyoruz.</h1>
  <p>Mükemmel Sayı Bulma Uygulaması</p>
</div>
<?php
function MukemmelSayiBuluyoruz($sayi) {
   if(!is_numeric($sayi)) {
      print "sayi?";
      return false;
   }
   for($a=1; $a<$sayi; $a++) {
      $sonuc = $sayi%$a;
      if($sonuc==0) {
         $dizi[]=$a;
      }
   }
   if(array_sum($dizi)==$sayi) {
       if($sayi!=null){
           
           echo '<script language="javascript">';
echo 'alert("Mükemmel Sayıdır")';
echo '</script>';
       }

      
   }
   else {
        if($sayi!=null){
   echo '<script language="javascript">';
echo 'alert("Mükemmel Sayı Değildir.")';
echo '</script>';
   }
   }
}
?>

 <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST")
        {
           
            $msayi=$_POST['msayi'];
            echo "<h3> Son Girilen Sayı : $msayi</h3>";
            
        }
        
       MukemmelSayiBuluyoruz((int)$msayi);
    ?>

<div>
  <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    <label for="fname">Mükemmel Sayı Mı?</label>
    <input type="text" id="msayi" name="msayi" placeholder="Sayıyı Giriniz..">
    <input type="submit" value="Gönder">
  </form>
</div>
</body>
</html>
