<?php
require 'dbconnect.php';

$sql = "UPDATE orders SET completed=TRUE WHERE order_id = $_POST[id]";
 if ($conn->query($sql) === TRUE) {
 }
 else {
   echo "ERROR";
 }

?>
