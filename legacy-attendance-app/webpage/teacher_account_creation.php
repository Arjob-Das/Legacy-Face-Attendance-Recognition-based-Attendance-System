<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teacher Register</title>
    <link rel="stylesheet" href="style2.css">
</head>

<body>
<div class="outerbox">
        <div class="innerbox">
        <header class="te-header">
                <h1>Teachers' Registration Form</h1>
            </header>
            <main class="te-body">
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
        <input type="text" id="teachid" name="teachid" required>
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
        <label for="dept">Department :</label>
        <input type="text" id="dept" name="dept" required>
        </p>
<p>
        <label for="assigned_class">Assigned Class:</label>
        <input type="text" id="assigned_class" name="assigned_class" required>
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
                *Image File Must be in jpeg/png format
        </p>
<p>
        <input type="submit" id="submit" value="SUBMIT">
</p>
    </form>
</main>
</div>
        <div class="square c1"></div>
        <div class="square c2"></div>
    </div>
</body>

</html>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $id=$_POST["teachid"];
    $fname=$_POST["fname"];
    $lname=$_POST["lname"];
    $cyr=$_POST["cyr"];
    $styr=$_POST["styr"];
    $dept=$_POST["dept"];
    $assigned_class=$_POST["assigned_class"];
    $tad=$_POST["tad"];


    $target_dir = __DIR__ . "/ImagesT/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0755, true);
    }
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    $uploadOk = 1;
    $ext = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

    if ($ext !== 'gif' && $ext !== 'png' && $ext !== 'jpg' && $ext !== 'jpeg') {
        $uploadOk = 0;
    }
    if ($uploadOk == 0) {
        exit('<script>alert("Sorry, your file was not uploaded due to type mismatch.")</script>');
    } else {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
            echo '<script>alert("The file has been uploaded.")</script>'; 
        } else {
            echo '<script>alert("Sorry, there was an error uploading your file.")</script>';
        }
        rename($target_file, $target_dir . $id . ".jpg");
    }

    $command_exec = "python image_uploader_T.py";
    $str_output = shell_exec($command_exec);
    
    $command_exec = "python adddatateacher.py " . 
                    escapeshellarg($fname) . " " . 
                    escapeshellarg($lname) . " " . 
                    escapeshellarg($id) . " " . 
                    escapeshellarg($cyr) . " " . 
                    escapeshellarg($styr) . " " . 
                    escapeshellarg($assigned_class) . " " . 
                    escapeshellarg($tad) . " " . 
                    escapeshellarg($dept);
    $str_output = shell_exec($command_exec);
}
?>