<html>
<head><basefont face="Arial"></head>
<body>
<h1>Test connection to MySQL Database<h1>
<?php
// Define variables
$servername = "localhost";
$username = "rudhamla_dave";
$password = "yjII71KXY5Ns";
$mydb = "rudhamla_rally";

// Create connection
$conn = new mysqli($servername, $username, $password, $mydb);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// sql to create table
$sql = "CREATE TABLE Persons (
   id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
   firstname VARCHAR(30) NOT NULL,
   lastname VARCHAR(30) NOT NULL,
   email VARCHAR(50),
   reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
  echo "Table Persons created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

// Create tables
// $sql = "SHOW DATABASES";
// $result = $conn->query($sql);
// echo "Keys: " . var_dump($result) . "<br>";

// if ($result->num_rows > 0) {
  // output data of each row
/*   $row = 0;
  while($row <= $result->num_rows) {
    echo "Database: " . $result[$row]. "<br>";
	$row++;
  }
} else {
  echo "0 Databases";
} */

// Create database
/* $sql = "SELECT * FROM test";
$result = $conn->query($sql);
var_dump($result);
echo "<br>";

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo $row . "<br>";
  }
} else {
  echo "0 results";
} */

// echo "Connected successfully";

$conn -> close();

?>

</body>
</html>