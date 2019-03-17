<?php
header('Content-Type:text/json;charset=UTF-8');
$json = <<<EOF
[{"Count":0,"TypeId":30,"TypeName":"促销信息"},{"Count":0,"TypeId":33,"TypeName":"退货退款"},{"Count":0,"TypeId":34,"TypeName":"作品被购买"},{"Count":0,"TypeId":36,"TypeName":"纪念日提醒"},{"Count":0,"TypeId":37,"TypeName":"系统公告"},{"Count":0,"TypeId":41,"TypeName":"订单提醒"}]
EOF;
echo  $json;