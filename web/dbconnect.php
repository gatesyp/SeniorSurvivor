<?php
$servername = 'stoh.io';
$username = 'fashionksu';
$password = 'lollipop123';
$dbname = 'seniorsurvivor';

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection Failed: " . $conn->connect_error);
}
?>
