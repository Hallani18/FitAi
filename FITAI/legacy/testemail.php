<?php
	$message = "this is an smptp protocol sent email.";
	$headers ="From: 11fitnessai11@gmail.com";
	mail("aismail123@gmail.com", "Testing", $message, $headers);
	echo "this is a reminder to eat your veggies"
?>