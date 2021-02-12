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
  <h1>En Büyük Tek Sayıyı Buluyoruz.</h1>
  <p>En Büyük Tek Sayıyı Bulma Uygulaması</p>
</div>
<?php
function EnBuyukTekSayi($sayi) {
$sayilar  =$sayi;
$sayidizisi = explode(",", $sayilar);
rsort($sayidizisi);

for ($i = 0; $i < count($sayidizisi); $i++) {
 
  if($sayidizisi[$i]%2!=0){
      
      $enbuyuk=$sayidizisi[$i];
      break;
  }
   
}

 if($sayi!=null){
echo "En buyuk sayi: ".$enbuyuk;

}
}

?>

 <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST")
        {
           
            $teksayi=$_POST['teksayi'];
            echo "<h3> Son Girilen Sayı : $teksayi</h3>";
            
        }
       EnBuyukTekSayi($teksayi);
    ?>
<div>
  <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    <label for="fname">Sayı Dizisini Giriniz:</label>
    <input type="text" id="teksayi" name="teksayi" placeholder="Sayi Dizisini Giriniz Örnek: 1,2,3,4,5,6">
    <input type="submit" value="Gönder">
  </form>
</div>
</body>
</html>
