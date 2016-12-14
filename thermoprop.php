/** 
* calculate.php
* 
* 热力计算模块
* @author      Robin
* @version     1.0
*/

<?php
require_once 'hprose/Hprose.php';

use Hprose\Client;
# use Hprose\InvokeSettings;
# use Hprose\ResultMode;

$client = Client::create('http://127.0.0.1:8181/',false);

switch ($_GET["calc_type"])
{
    case 'Sat_T':
    echo $client->sat_T(floatval($_GET["press"]), floatval($_GET["quality"]));
    break;
    case 'Sat_P':
    echo $client->sat_P(floatval($_GET["temp"]), floatval($_GET["quality"]));
    break;
    case 'h':
    echo $client->prop_sw(floatval($_GET["press-h"]), floatval($_GET["temp-h"]));
    break;
    default:
    echo "Error";

}
// echo $client->sat_T(floatval($_GET["press"]), floatval($_GET["quality"]));

// # echo $res
?>