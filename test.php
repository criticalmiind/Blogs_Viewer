<?php
echo rand(5, 7);
echo 'Gecko/' . date('Ymd', rand(strtotime('2011-1-1'), time())) . ' Firefox/' . rand(5, 7) . '.0';
?>