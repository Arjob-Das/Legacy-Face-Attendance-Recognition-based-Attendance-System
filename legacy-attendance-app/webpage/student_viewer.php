<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Information Viewer</title>
    <link rel="stylesheet" href="style4.css">
    <link rel="stylesheet" href="style3.css">
</head>
<body>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
        <h1>Student Information Viewer</h1>
        <label for="studid">Enter Student ID:</label>
        <input type="number" id="studid" name="studid" required>
        <input type="submit" name="sub" value="SUBMIT">
    </form>

<?php
if (isset($_POST['sub'])){
    $id = $_POST["studid"];
    $command_exec = "python studentview.py " . escapeshellarg($id);
    $str_output = shell_exec($command_exec);
    
    $data = json_decode($str_output, true);

    echo "<center>";
    if (!$data || isset($data['error'])) {
        echo "<h2 style='color: red;'>Error: Student with ID " . htmlspecialchars($id) . " not found.</h2>";
    } else {
        $id = $data['id'];
        $name = $data['name'];
        $total = $data['total_attendance'];
        $standing = $data['standing'];
        $major = $data['major'];
        $year = $data['year'];
        $starting_yr = $data['starting_year'];
        $lst_at_time = $data['last_attendance_time'];

        echo "<h2>Student Profile</h2>";
        echo "<img src='Images/$id.jpg' alt='Student Image' style='max-width: 200px; border-radius: 10px;'>";
        echo "<br><br>";
        echo "<strong>ID:</strong> ", htmlspecialchars($id);
        echo "<br>";
        echo "<strong>Name:</strong> ", htmlspecialchars($name);
        echo "<br>";
        echo "<strong>Total Attendance:</strong> ", htmlspecialchars($total);
        echo "<br>";
        echo "<strong>Major:</strong> ", htmlspecialchars($major);
        echo "<br>";
        echo "<strong>Standing:</strong> ", htmlspecialchars($standing);
        echo "<br>";
        echo "<strong>Year:</strong> ", htmlspecialchars($year);
        echo "<br>";
        echo "<strong>Starting Year:</strong> ", htmlspecialchars($starting_yr);
        echo "<br>";
        echo "<strong>Last Attendance Time:</strong> ", htmlspecialchars($lst_at_time);
    }
    echo "</center>";
}
?>
</body>
</html>