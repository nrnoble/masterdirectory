<? php

$f3->route ('POST|GET /upload',
    function($f3)
    {

        // Reference. upload script from https://www.w3schools.com/php/php_file_upload.asp
        $profile = $_SESSION['Profile-data'];
        //print_r($_SESSION);
        //$target_dir = $_SERVER['DOCUMENT_ROOT'] ."/328/signup/images/";
        $target_dir = "./images/";

        $imageFileName = $target_dir . basename($_FILES["fileToUpload"]["name"]);

        // Optional uncomment to create a F3 var. Not required for upload to be successful.
//     $f3->set(imagePath,$imageFileName);

        $uploadOk = 1;
        $imageFileType = pathinfo($imageFileName,PATHINFO_EXTENSION);

        // Check if image file is a actual image or fake image
        if(isset($_POST["submit"])) {
            $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
            if($check !== false) {
                echo "File is an image - " . $check["mime"] . ".";
                $uploadOk = 1;

            } else {
                echo "File is not an image.";
                $uploadOk = 0;
            }
        }

        // Check if file already exists
        if (file_exists($imageFileName)) {
            echo "Sorry, file already exists.";
            $uploadOk = 0;
            $_SESSION['imagePath'] = $imageFileName;
        }

        // Check file size
        if ($_FILES["fileToUpload"]["size"] > 500000) {
            echo "Sorry, your file is too large.";
            $uploadOk = 0;
        }

        // Allow only certain image formats
        if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
            && $imageFileType != "gif" ) {
            echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
            $uploadOk = 0;
        }

        // Check if $uploadOk is set to 0 by an error
        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded.";
            // if everything is ok, try to upload file
        }
        else {
            // target_file
            if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $imageFileName)) {
                echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
                // create a session var with url path to image file
                $_SESSION['imagePath'] = $imageFileName;
            } else {
                //  echo "Sorry, there was an error uploading your file.";
            }
        }


        $view = new View;

        // IMPORTANT
        // The following two lines much be modified
        // to create a valid Fatfree route for the current application
        echo $view->render('/pages/home.php');
        header('Location: /328/upload/');


 });



















?>