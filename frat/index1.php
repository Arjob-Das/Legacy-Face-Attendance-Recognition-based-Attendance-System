<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<link rel="stylesheet" href="style1.css">

<body>
    <form>
        <h2>Registration Form</h2>
        <label for="fullname">Full Name:</label>
        <input type="text" id="fullname" name="fullname" required>
        <label for="id">ID:</label>
        <input type="number" id="studid" name="studid" required>
        <label for="year">Starting Year:</label>
        <input type="date" id="styr" name="stry" required>
        <label for="major">Major:</label>
        <input type="text" id="major" name="major" required>
        <label for="Attendance">Total Attendance:</label>
        <input type="number" id="tad" name="tad" required>
        <label for="imageInput">Upload your image:</label>
        <input type="file" id="imageInput" name="image">
        <button type="submit">Submit</button>
    </form>

</body>

</html>