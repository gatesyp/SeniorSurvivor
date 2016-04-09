<?php
require 'dbconnect.php';


function make_order_table($result) {
  require 'dbconnect.php';
  print '<div class="table-responsive">' . "\n";
  $colors = array(0 => 'success', 'warning', 'danger', 'info');
  $last_room = -1;
  $color = 0;
print '<table id="ordertable" class="table table-hover">' . "\n";

$row = $result->fetch_assoc();
print " <tr> \n";
foreach ($row as $field => $value){
 print " <th>$field</th> \n";
}
print " </tr> \n";

foreach($result as $row){

 $room = $row["room"];
 if (abs($room-$last_room) < 6 || $last_room == -1 ) {
   print " <tr class=\"$colors[$color]\"> \n";
 }
   else {
     if ($color < 3) {
       $color++;
     }
     else {
       $color = 0;
     }
     print " <tr><td /><td /><td /><td /><td /><td /><td /><td /></tr> \n";
     print " <tr class=\"$colors[$color]\"> \n";
   }
   $last_room = $room;
   $order = $row["order_id"];
   $itemid = $row["item_id"];

   $sql = "SELECT name FROM items WHERE id=" . $itemid;
   $itemresult = $conn->query($sql);
   $itemrow = $itemresult->fetch_assoc();
   $item = $itemrow["name"];
   $quantity = $row["quantity"];
   $name = $row["name"];
   $room = $row["room"];
   $extras = $row["extras"];
   $completed = $row["completed"];
   $time = date('h:i A',strtotime($row["time"]));
   print " <td class = 'order_id'>$order</td> \n";
   print " <td class = 'item'>$item</td> \n";
   print " <td class = 'quantity'>$quantity</td> \n";
   print " <td class = 'name'>$name</td> \n";
   print " <td class = 'room'>$room</td> \n";
   print " <td class = 'completed'>$completed</td> \n";
   print " <td class = 'time'>$time</td> \n";
   print " <td class = 'extras'>$extras</td> \n";
 print " </tr> \n";
}
print "</table> \n";
print "</div> \n";

}

//////////////////////////////////////////////////////////////////////////////////////////////
function make_item_table($result) {
print '<div class="table-responsive">' . "\n";
print '<table id="tableitems" class="table table-hover">' . "\n";

$row = $result->fetch_assoc();

print " <tr> \n";
foreach ($row as $field => $value){
 print " <th>$field</th> \n";
}
print " </tr> \n";

foreach($result as $row){
  print " <tr> \n";
  $id = $row["id"];
  $name = $row["name"];
  $price = $row["price"];
  $available = $row["available"];

  print " <td class = 'id'>$id</td> \n";
  print " <td class = 'name'>$name</td> \n";
  print " <td class = 'price'>$price</td> \n";
  print " <td class = 'available'>$available</td> \n";

  print " </tr> \n";
}

print "</table> \n";
print "</div> \n";

}
?>
