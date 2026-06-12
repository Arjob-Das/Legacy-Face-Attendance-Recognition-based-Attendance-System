<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="style4.css">
</head>
<body>
    
           
    <form method="post" enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF'];?>">
    <h1>Registration Form</h1>
        <label for="id">Enter Student ID:</label>
        <input type="number" id="studid" name="studid" required>
        <input type="submit" name="sub" value="SUBMIT">
    </form>

</body>

</html>
<?php
if (isset($_POST['sub'])){
    $id=$_POST["studid"];
    $command_exec = escapeshellcmd("python studentview.py $id");
    $str_output = shell_exec($command_exec);
    
        header("Location: student_login.php");
        exit();

}
?>