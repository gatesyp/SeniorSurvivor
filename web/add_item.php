<?php
error_reporting(-1);
require 'dbconnect.php';
require 'table.php';
 ?>

  <!DOCTYPE html>
  <html lang="en">

  <head>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <!--<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"> -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Senior Survivor Dashboard</title>
  </head>

  <body>

    <div class="container">
      <?php include 'navbar.php';
        ?>
<form action="item_handler.php" id="itemform" method="post">
  <input style="display:none" type="text" name="type" value="add_item" />
 <div class="form-group">
   <label for="name">Item Name</label>
   <input type="text" class="form-control" name="name" id="name" placeholder="Name">
      </div>
      <div class="form-group">
        <label for="aliases">Aliases</label>
        <input type="text" class="form-control" name="aliases" id="aliases" placeholder="Alias, Alias 2, Alias 3">
        <span class="help-block">Include as many aliases as possible in order to improve twitter product recognition</span>
           </div>
      <div class="form-group" id="priceform">
     <label for="price">Price</label>
     <div class="input-group">
       <div class="input-group-addon">$</div>
       <input type="text" class="form-control" name="price" id="price" placeholder="0.00">
     </div>
           <span class="help-block">Any price between 0.00 and 99.99</span>
   </div>
 <button type="submit" class="btn btn-default">Submit</button>
</form>
<script>

$('#itemform').on('submit', function(e) {

    var name = $('#name')
    var aliases = $('#aliases')
    var price = $('#price')


    if (name.parent().hasClass("has-error") || aliases.parent().hasClass("has-error") || price.parent().hasClass("has-error")) {
      e.preventDefault();

    }

});

$('#name').blur(function() {
  if ( !$(this).val() ) {
        $(this).parent().removeClass("has-success");
        $(this).parent().addClass("has-error");
  }
  else {
    $(this).parent().removeClass("has-error");
    $(this).parent().addClass("has-success");
  }
});

$('#aliases').blur(function() {
  if (1 == 0) {
        $(this).parent().removeClass("has-success");
        $(this).parent().addClass("has-error");
  }
  else {
  $(this).parent().removeClass("has-error");
    $(this).parent().addClass("has-success");
  }
});

$('#price').blur(function() {
  var moneyReg = /^\d{0,2}(\.\d{0,2})?$/
  var price = $('#price').val();
  if (!moneyReg.test(price) || !price) {
        $(this).parent().removeClass("has-success");
        $(this).parent().addClass("has-error");
  }
  else {
    $(this).parent().removeClass("has-error");
    $(this).parent().addClass("has-success");
  }
});

</script>
  </body>

  </html>
