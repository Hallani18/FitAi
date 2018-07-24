<?php  session_start();  // session starts with the help of this function 
$db = new PDO('sqlite:C:\xampp\htdocs\FITAI\fitai.db') or die("ERROR ERROR");

if(isset($_SESSION['user'])) 
{
	header("Location:home.php"); 
}

if(isset($_POST['login']))   // it checks whether the user clicked login button or not 
{
    $user = $_POST['user'];
    $pass = $_POST['pass'];
	$query="SELECT username, password FROM people WHERE (username='$user' AND password ='$pass')";
	$result= $db->query($query);
	$row = $result->fetch(PDO::FETCH_ASSOC);
		#$userdb=$row["username"];
		#$passdb=$row["password"];
		$password=$row['username'];
		$username=$row['password'];
	
    if ($username!="")
	{
        if ($password==$pass)
		{
           $_SESSION["login"]=$user;
		   #echo "SUCCESS \n";
           header('Location: home.php');


         #echo '<script type="text/javascript"> window.open("home.php","_self");</script>';            //  On Successful Login redirects to home.php

        }
	}

        else
        {
			echo "Incorrect information";
            #echo $username; 
			#echo $password;
			#header("Location:home.php");	
        }
}
 ?>
 <html>
	<head>
		<title>Fit AI</title>
		<link rel="stylesheet" href="./css/style_for_login_and_website.css">
	</head>

	<body>
		</div>
		<div class="login-page">
			<div class="form">
				<form class="Login-form" method="post" action="../../cgi-bin/login.php"">
						<input type="text" placeholder="username" name="username"/>
						<input type="password" placeholder="password" name="password"/>
						<button type="submit"  name="Login">login</button>
						<p class="message"><a href="#">Register</a></p>
					</form>
			</div>
		</div>

			
	</body>
</html>
