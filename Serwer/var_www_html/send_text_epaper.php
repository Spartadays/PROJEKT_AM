<?php
    if(isset($_GET["text"]))
    {
        $text = $_GET["text"];
    }
    $command = "sudo /usr/bin/python3 /var/www/html/send_text_epaper.py ".$text;
    echo shell_exec($command);
?>