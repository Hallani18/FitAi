<?php
session_start();
$db = new PDO('sqlite:C:\xampp\htdocs\FITAI\fitai.db') or die("ERROR ERROR");
if(isset($_SESSION['user']) != TRUE)
{		
	$a=1;
		#header("Location:login.php");
}
?>