
<?php
$command_exec = escapeshellcmd('python stud_face.py');
$str_output = shell_exec($command_exec);
echo"<script>alert( 'Attendance Updated Successfully')</script>";

echo "<link rel='stylesheet' href='style3.css'>";
echo "<center>";
echo "<h1> Attendance </h1>";

echo "Updated Attendance : ", $str_output;
echo "<a href='student_login.php' class='my-btn' rel='noopener noreferrer'>Back to Login</a>";
echo "</center>";
#header("Location: student_viewer.php");
exit();
?>