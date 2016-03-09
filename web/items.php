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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Senior Survivor Dashboard</title>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
       <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
       <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
     <![endif]-->
  </head>

  <body>

    <div class="container">
      <?php include 'navbar.php';
        $sql = "SELECT * FROM items";
        $result = $conn->query($sql);
        make_item_table($result);
        ?>
      <a class="btn btn-default" href="add_item.php" role="button">Add Item</a>
      </div>

  </body>
  <script>
  $(document).ready(function() {
    $("div.container table").delegate('tr', 'click', function() {
      var id = ($(this).find("td.id").html());
      $('div.container').html('<form action="edit_item.php" name="edit" method="post" style="display:none;"><input type="text" name="id" value="' + id + '" /></form>');
      document.forms['edit'].submit();
    });
  });
</script>

  </html>
