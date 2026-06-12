
<?php
$command_exec = escapeshellcmd('python test.py');
$str_output = shell_exec($command_exec);
echo "Attendance Updated Successfully";
?>