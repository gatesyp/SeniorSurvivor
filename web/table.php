<?php


function make_order_table($result) {
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
     print " <tr><td /><td /><td /><td /><td /><td /><td /></tr> \n";
     print " <tr class=\"$colors[$color]\"> \n";
   }
   $last_room = $room;
 foreach ($row as $value){
 print " <td>$value</td> \n";
 }
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
