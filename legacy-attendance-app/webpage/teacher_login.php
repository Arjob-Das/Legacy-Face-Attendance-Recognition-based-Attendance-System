<?php
$command_exec = escapeshellcmd('python logintch.py');
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
$assigned_class = $data['assigned_class'];
$dept = $data['department'];
$year = $data['year'];
$starting_yr = $data['starting_year'];
$lst_at_time = $data['last_attendance_time'];

echo "<center>";
echo "<h1> Teacher Information </h1>";

echo "<img src='ImagesT/$id.jpg' alt='Teacher Image'>";
echo "<br>";
echo "ID : ", $id;
echo "<br>";
echo "Name : ", $name;
echo "<br>";
echo "Total Attendance : ", $total;
echo "<br>";
echo "Department : ", $dept;
echo "<br>";
echo "Assigned Class : ", $assigned_class;
echo "<br>";
echo "Year : ", $year;
echo "<br>";
echo "Starting Year : ", $starting_yr;
echo "<br>";
echo "Last Attendance Time : ", $lst_at_time;
echo "<br> <br> <br>";
echo "<link rel='stylesheet' href='style3.css'>";
echo "<a href='attendanceT.php' class='my-btn' rel='noopener noreferrer'>Give Attendance</a>";
echo "<a href='student_viewer.php' class='my-btn' target='_blank' rel='noopener noreferrer'>View Student Info</a>";
echo "</center>";
?>