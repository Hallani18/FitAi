<?php  session_start();  // session starts with the help of this function 
$db = new PDO('sqlite:C:\xampp\htdocs\FITAI\fitai.db') or die("ERROR ERROR");

if(isset($_SESSION['user'])) 
{
	header("Location:home.php"); 
}

if(isset($_POST['login']))   // it checks whether the user clicked login button or not 
{
    $user = $_POST['username'];
    $pass = $_POST['password'];
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
		<dev class="container">
			<video poster="./images/background-pic.jpg" autoplay="true" loop="true">
				<source src="./videos/background_video_with_audio.mp4" type="video/mp4">
				<source src="./videos/background_video_with_audio.webm" type="video/webm">
			</video>
		</div>
		<div class="login-page">
			<div class="form">
				<form class="register-form" method="post" action="../../cgi-bin/hw.cgi"">
					<img src="./images/logo2.png">
					<br>
					<br>
					<input type="text" placeholder="Username"name="username"><br>
					<input type="text" placeholder="Firstname" name="firstname"><br>
					<input type="text" placeholder="Surname" name="surname"><br>
					<input type="password" placeholder="Password" name="password"><br>
					<input type="email" placeholder="Email" name="email"><br>
					<button type="submit"  value="Submit">Submit</button>
					<p class="message">Already a Member?<a href="#">Login here</a>
				</form>

	
					<form class="Login-form" method="post" action="login.php"">
						<img src="./images/logo2.png">
						<br>
						<br>
						<input type="text" placeholder="username" name="username"/>
						<input type="password" placeholder="password" name="password"/>
						<button type="submit"  name="login">login</button>
						<p class="message"><a href="#">Register</a></p>
					</form>
			</div>
		</div>
		<script src="https://code.jquery.com/jquery-3.3.1.min.js">
		</script>

		<script type="text/javascript">
			$('.message a').click(function(){
			$('form').animate({height:"toggle",opacity: "toggle"}, "slow");
			});
		</script>
			
	</body>
</html>
