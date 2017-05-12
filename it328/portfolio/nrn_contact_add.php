<?php
    session_start();
    //$servername = gethostname();
    //$username = get_current_user();
    //$password = getpwd();

    // Create connection
    $conn = new mysqli("127.0.0.1", "nnoble_nrnoble", 'J$p1ter2',"nnoble_portfolio");

    // Check connection
    if ($conn->connect_error)
    {

        #echo "He is dead jim";
        die("Connection failed: " . $conn->connect_error);

    }
    else
    {
        # print_r($_SESSION);
        # echo "done";
    }

    $name = $_SESSION['name'];
    $email = $_SESSION['email'];
    $comments = $_SESSION['comments'];


    $sql = "INSERT INTO `nnoble_portfolio`.`contacts` (`name`, `email`, `comments`,`date`) VALUES ('$name', '$email', ' $comments', CURRENT_TIMESTAMP)";
    #echo"$sql";
    $conn->query($sql);
    if (!$result->field_count < 1 )
    {
        echo "<h2 style = 'color:red'>";
        echo "<p>Error: " . mysqli_error($conn) . "</p>";
        print_r($_POST);
        echo "</h2>";
        return;

    }
    else
    {
        header("Location: index.php");
    }


?>