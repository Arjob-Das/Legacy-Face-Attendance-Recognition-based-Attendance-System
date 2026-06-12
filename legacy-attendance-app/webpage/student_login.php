<?php
$command_exec = escapeshellcmd('python loginpt.py');
$str_output = shell_exec($command_exec);
#echo $str_output;
$data = json_decode($str_output, true);

if (!$data || isset($data['error'])) {
    echo "<center>";
    echo "<link rel='stylesheet' href='style.css'>";
    exit("<h1>Unable to Verify Login</h1>");
}

$id = $data['id'];
$name = $data['name'];
$total = $data['total_attendance'];
$standing = $data['standing'];
$major = $data['major'];
$year = $data['year'];
$starting_yr = $data['starting_year'];
$lst_at_time = $data['last_attendance_time'];

echo "<link rel='stylesheet' href='style3.css'>";
echo "<center>";
echo "<h1> Student Information </h1>";

echo "<img src='Images/$id.jpg' alt='Student Image'>";
echo "<br>";
echo "ID : ", $id;
echo "<br>";
echo "Name : ", $name;
echo "<br>";
echo "Total Attendance : ", $total;
echo "<br>";
echo "Major : ", $major;
echo "<br>";
echo "Standing : ", $standing;
echo "<br>";
echo "Year : ", $year;
echo "<br>";
echo "Starting Year : ", $starting_yr;
echo "<br>";
echo "Last Attendance Time : ", $lst_at_time;
echo "<br> <br> <br>";
echo "<a href='attendance.php' class='my-btn' rel='noopener noreferrer'>Give Attendance</a>";
echo "</center>";
?>