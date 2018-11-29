<?php
$text = htmlspecialchars($_REQUEST["text"], ENT_QUOTES); 
?>
<!DOCTYPE html>
<html>
<head>
    <title>XSS Text</title>
</head>
<body>
<form action="index_secure.php" method="post">
    Text:  <input type="text" name="text" /><br />
            <input type="submit" value="Change text"/>
</form>
    <div>
        <span title="<?php echo $text ?>">
            Hover to see text.
        </span>
    </div>
</body>
</html>
