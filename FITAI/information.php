<?php
require("session.php");
if(isset($_POST['submit']))
{
	$gender = $_POST['gender'];
	$age = $_POST['age'];
	$feet = $_POST['feet'];
	$inches = $_POST['inches'];
	$ftin = $feet.'"'.$inches;
	$lbs = $_POST['lbs'];
	
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
				
					<form class="Information-form" method="post" action="information.php"">
						<img src="./images/logo2.png">
						<br>
						
						<br>
						
						Male<input type="radio" name="gender" value="0" checked> Female
						<input type="radio" name="gender" value="1" >Age<br>
						<select name="age">
							<option value="13">13</option>
							<option value="14">14</option>
							<option value="15">15</option>
							<option value="16">16</option>
							<option value="17">17</option>
							<option value="18">18</option>
							<option value="19">19</option>
							<option value="20">20</option>
							<option value="21">21</option>
							<option value="22">22</option>
							<option value="23">23</option>
							<option value="24">24</option>
							<option value="25">25</option>
							<option value="26">26</option>
							<option value="27">27</option>
							<option value="28">28</option>
							<option value="29">29</option>
							<option value="30">30</option>
						</select>
						<br> <br>
						<input type="number" min="1" max="9" onkeydown="return false" name="feet" placeholder="feet">
						<input type="number" min="0" max="11" onkeydown="return false" name="inches" placeholder="inches">
						<input type="number" min="1" max="800" onkeydown="return false" name="lbs" placeholder="lbs">
						<button type="submit"  name="submit">submit</button>
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
