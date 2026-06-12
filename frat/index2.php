<?php
$command_exec = escapeshellcmd('python loginpt.py');
$str_output = shell_exec($command_exec);
#echo $str_output;
$ar=explode(" ",$str_output);
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
$standing=$ar[$c];
$c=$c+3;
$year=$ar[$c];
$c=$c+3;
$starting_yr=$ar[$c];
$c=$c+3;
$lst_at_time=$ar[$c]." ".$ar[$c+1];
echo "<center>";
echo "<h1> Student Information </h1>";

echo "<img src='Images/$id.jpg'></img>";
echo "<br>";
echo "ID : ",$id;
echo "<br>";
echo "Name : ",$name;
echo "<br>";
echo "Total Attendance : ",$total;
echo "<br>";
echo "Standing : ",$standing;
echo "<br>";
echo "Year : ",$year;
echo "<br>";
echo "Starting Year : ",$starting_yr;
echo "<br>";
echo "Last Attendance Time : ",$lst_at_time;
echo "<br> <br> <br>";
echo "<a href='attendance.php' class='my-btn' target='_blank'><input type='button' name ='Give Attendance' value='Give Attendance'></a>";
#echo "<a href='attendance.php' class='my-btn' target='_blank'>Register Yourself</a>";
#echo "</input>";
echo "</center>";
?>