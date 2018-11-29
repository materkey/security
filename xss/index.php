<?php
  $text = $_REQUEST['text'];
?>
<!DOCTYPE html>
<html>
<head>
    <title>XSS Text</title>
</head>
<body>
<form action="index.php" method="post">
Text:  <input type='text' name='text'>
<br/>  <input type="submit" value="Change text"/>
</form>
    <div>
        <span title=<?php echo $text ?>>
            Hover to see text.
        </span>
    </div>
</body>
</html>
