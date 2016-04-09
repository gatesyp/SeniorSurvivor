<?php
require 'dbconnect.php';
if ($_POST['type'] == "add_item") {
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
 print ('<a class="btn btn-default" href="add_item.php" role="button">Add Another Item</a>');
 print('<a class="btn btn-default" href="items.php" role="button">Return to Items</a>');
/////////////////////////////////////////////////////////////

 } else if ($_POST['type'] == "edit_item") {
   $available = "False";
   if (isset($_POST['available'])) {
     $available = "True";
   }
   $sql = "UPDATE items SET name='$_POST[name]', price='$_POST[price]', available='$available' WHERE id = $_POST[id]";
   if ($conn->query($sql) === TRUE) {
     echo "Item Updated in database! <br>";

     $aliases = explode(',', "$_POST[aliases]");
     $aliases = array_map('trim', $aliases);
     var_dump($aliases);

     $item_id = $_POST['id'];
     $sql = "SELECT alias FROM aliases WHERE item_id = $item_id";
     $result = $conn->query($sql);
     $row = $result->fetch_assoc();
     $db_aliases = [];
     foreach($result as $row) {
       $db_aliases[] = $row["alias"];
     }

     foreach ($db_aliases as $db_alias) {
       $found = False;
       foreach ($aliases as $key => $alias) {
         if ($db_alias == $alias) {
           $found = True;
           unset($aliases[$key]);
         }
       }

       if ($found === False){
         $sql = "DELETE FROM aliases WHERE alias='$db_alias'";
          if ($conn->query($sql) === TRUE) {
            echo "old alias removed from database";
       } else {
         echo "Error: " . $sql . "<br>" . $conn->error;
       }
      }
     }

     foreach($aliases as $alias) {
       var_dump($alias);
     $sql = "INSERT INTO aliases (item_id, alias) VALUES ($item_id, '$alias')";
     if ($conn->query($sql) === TRUE) {
       echo "Alias Added <br>";
     } else {
       echo "Error: " . $sql . "<br>" . $conn->error;
     }
   }



 } else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
 print('<a class="btn btn-default" href="items.php" role="button">Return to Items</a>');
}
?>
