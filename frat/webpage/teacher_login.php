<?php
$command_exec = escapeshellcmd('python logintch.py');
$str_output = shell_exec($command_exec);
#echo $str_output;
$ar=explode(" ",$str_output);
if ($ar[0]=="Login"){
    echo "<cetner>";
    echo "<link rel='stylesheet' href='style.css'>";
    exit("<h1>Unable to Verify Login</h1>");
}
$id=$ar[0];
$c=3;
$name=$ar[$c];
$c=$c+1;
#echo is_numeric("119");
while (is_numeric($ar[$c])!=true){
    $name=$name." ".$ar[$c];
    $c=$c+1;    
}

$total=$ar[$c];
$c=$c+3;
$assigned_class=$ar[$c];
$c=$c+3;
$dept=$ar[$c];
$c=$c+1;
while (is_numeric($ar[$c])!=true){
    $dept=$dept." ".$ar[$c];
    $c=$c+1;    
}
$year=$ar[$c];
$c=$c+3;
$starting_yr=$ar[$c];
$c=$c+3;
$lst_at_time=$ar[$c]." ".$ar[$c+1];

echo "<center>";
echo "<h1> Teacher Information </h1>";

echo "<img src='ImagesT/$id.jpg'></img>";
echo "<br>";
echo "ID : ",$id;
echo "<br>";
echo "Name : ",$name;
echo "<br>";
echo "Total Attendance : ",$total;
echo "<br>";
echo "Department : ",$dept;
echo "<br>";
echo "Assigned Class : ",$assigned_class;
echo "<br>";
echo "Year : ",$year;
echo "<br>";
echo "Starting Year : ",$starting_yr;
echo "<br>";
echo "Last Attendance Time : ",$lst_at_time;
echo "<br> <br> <br>";
echo "<link rel='stylesheet' href='style3.css'>";
echo "<a href='attendanceT.php' class='my-btn' rel='noopener noreferrer'>Give Attendance</a>";
echo "<a href='student_viewer.php' class='my-btn' target='_blank' rel='noopener noreferrer'>View Student Info</a>";
echo "</center>";
?>