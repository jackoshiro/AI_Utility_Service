<html>
<head>
<title>PHP File Upload example</title>
</head>
<body>

<form action="index.php" enctype="multipart/form-data" method="post">
  Select image :
  <input type="file" name="file"><br/>
  <input type="submit" value="Upload JPG" name="Submit"> <br/>
</form>

<?php
  switch ($_POST['Submit']) {
    case 'Upload JPG':
      # $filepath = "images/" . $_FILES["file"]["name"];
      $filepath = "images/image.jpg";

      if(move_uploaded_file($_FILES["file"]["tmp_name"], $filepath)) {
        echo "<img src=$filepath?" . time() . "height=200 width=300 />";
        echo '<form action="http://192.168.200.33:5000/cgi-bin/step8_glasses_prediction.py" method="GET">
                <input type="hidden" name="form_submitted" value="1" />
                <input type="submit" value="Predict" name="Submit"> <br/>
              </form>';
      }
      else {
        echo "Error !!";
      }
      break;
    case 'Predict':
      break;
    default:
      break;
  }
?>

</body>
</html>
