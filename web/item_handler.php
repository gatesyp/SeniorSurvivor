<?php
require 'dbconnect.php';
$sql = "INSERT INTO items (name, price, available) VALUES ('$_POST[name]', $_POST[price], TRUE)";
 if ($conn->query($sql) === TRUE) {
   echo "Item Added to database! <br>";
   $sql = "SELECT id FROM items ORDER BY id DESC LIMIT 1";
   $result = $conn->query($sql);
   $row = $result->fetch_assoc();
   $id = $row['id'];
   $aliases = explode(',', "$_POST[aliases]");
   $aliases = array_map('trim', $aliases);

   foreach($aliases as $alias) {
   $sql = "INSERT INTO aliases (item_id, alias) VALUES ($id, '$alias')";
   if ($conn->query($sql) === TRUE) {
     echo "Alias Added <br>";
   } else {
     echo "Error: " . $sql . "<br>" . $conn->error;
   }
 }
 } else {
   echo "Error: " . $sql . "<br>" . $conn->error;
 }
 $conn->close();
?>

<a class="btn btn-default" href="add_item.php" role="button">Add Another Item</a>
<a class="btn btn-default" href="items.php" role="button">Return to Items</a>
