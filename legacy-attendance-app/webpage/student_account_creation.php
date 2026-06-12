<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Register</title>
    <link rel="stylesheet" href="style1.css">
</head>

<body>
    <div class="outerbox">
        <div class="innerbox">
        <header class="stu-header">
                <h1>Registration Form</h1>
        </header>
            <main class="stu-body">
    <form method="post" enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF'];?>">
<p>
        <label for="fname">First Name:</label>
        <input type="text" id="fname" name="fname" required>
</p>
<p>
        <label for="lname">Last Name:</label>
        <input type="text" id="lname" name="lname" required>
</p>
<p>
        <label for="id">ID:</label>
        <input type="number" id="studid" name="studid" required>
</p>
<p>
        <label for="current year">current Year:</label>
        <input type="text" id="cyr" name="cyr" required>
</p>
<p>
        <label for="starting year">Starting Year:</label>
        <input type="text" id="styr" name="styr" required>
</p>
<p>
        <label for="major">Major:</label>
        <input type="text" id="major" name="major" required>
</p>
<p>
        <label for="standing">Standing:</label>
        <input type="text" id="standing" name="standing" required>
</p>
<p>
        <label for="Attendance">Total Attendance:</label>
        <input type="number" id="tad" name="tad" required>
</p>
<p>
        <label for="imageInput">Upload your image:</label>
        <input type="file" name="fileToUpload" id="fileToUpload">
</p>
<p>
        *Image File must be in jpeg/png format
</p>
<p>
        <input type="submit" id="submit" value="SUBMIT">
</p>
                </main>
    </form>
</div>
        <div class="circle c1"></div>
        <div class="circle c2"></div>
    </div>
</body>

</html>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $id=$_POST["studid"];
    $fname=$_POST["fname"];
    $lname=$_POST["lname"];
    $cyr=intval($_POST["cyr"]);
    $styr=intval($_POST["styr"]);
    $major=$_POST["major"];
    $standing=$_POST["standing"];
    $tad=intval($_POST["tad"]);


    $target_dir = "C:/xampp/htdocs/legacy-attendance-app/webpage/Images";
    $target_file = $target_dir.basename($_FILES["fileToUpload"]["name"]);
    $uploadOk = 1;
    $ext = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

if ($ext !== 'gif' && $ext !== 'png' && $ext !== 'jpg'&& $ext !== 'jpeg') {
    $uploadOk=0;
}
    if ($uploadOk == 0) {
        exit ('<script>alert("Sorry, your file was not uploaded due to type mismatch.")</script>');
    // if everything is ok, try to upload file
    } else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo '<script>alert("The file has been uploaded.")</script>'; 
    } else {
        echo '<script>alert ("Sorry, there was an error uploading your file.")</script>';
    }
    rename($target_file,"$target_dir/$id.jpg");
}

        $command_exec = escapeshellcmd("python adddata.py $fname $lname $id $cyr $styr $standing $tad $major");
        $str_output = shell_exec($command_exec);
        $command_exec = escapeshellcmd("python image_uploader.py");
        $str_output = shell_exec($command_exec);

}
?>