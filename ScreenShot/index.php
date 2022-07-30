<?php
require "vendor/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;

class Twitter
{
    private static $t;
    private static $c;

    public static function getInstance()
    {

        if (self::$t == null) {
            self::$t = new Twitter();
        }
        return self::$t;
    }

    public function __construct()
    {
        self::$c = new TwitterOAuth(
            'oU3BzU6u0fJr6c5PEGuCwDNPu',
            'C2tWTinYi6eMXjz60mthm0lAHBuQE4Qsk88cnDH9ygWLSipPpp',
            '1478352645572239369-L3L2L624I7UczsvsifI2qRdnBhj65N',
            'MfYcUPPC0o7Y7kR3I5L2sWU3EWJaeLieif8CGrLkO1qMR'
        );
    }

    public function setTimestamp($userDate)
    {
        $date = explode(" ", $userDate);
        switch ($date[1]) {
            case "Jan":
                $month = "01";
                break;
            case "Feb":
                $month = "02";
                break;
            case "Mar":
                $month = "03";
                break;
            case "Apr":
                $month = "04";
                break;
            case "May":
                $month = "05";
                break;
            case "Jun":
                $month = "06";
                break;
            case "Jul":
                $month = "07";
                break;
            case "Aug":
                $month = "08";
                break;
            case "Sep":
                $month = "09";
                break;
            case "Oct":
                $month = "10";
                break;
            case "Nov":
                $month = "11";
                break;
            case "Dec":
                $month = "12";
                break;
        }

        $result = strtotime($date[3] . " " . $date[5] . "/" . $month . "/" . $date[2]);
        return $result;
    }

    public function set_tweet_time($time)
    {
        date_default_timezone_set("Asia/Tehran");
        $timeStamp = $this->setTimestamp($time);
        $true_format = date('g:i A · M d, Y', $timeStamp + date('Z'));
        return $true_format;
    }

    public function tweet_data($id)
    {
        $tweet_data = self::$c->get('statuses/show', [
            'id' => $id,
            'tweet_mode' => 'extended',
        ]);

        return $tweet_data;
    }
}

$tweet_id = $_REQUEST['id'];
$theme = $_REQUEST['theme'];
$w = $_REQUEST['w'];
$obj = Twitter::getInstance();
$data = $obj->tweet_data($tweet_id);

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/style.css">
    <style>
        body {
            unicode-bidi: bidi-override;
            font-family: 'Iransansregular';
            <?php echo "background-color: #" . $theme . ";"; ?>
        }

        #contentbox { 
            <?php echo "width: " . $w . "px;"; ?>
        }

        #contentbox {
            text-justify: inter-word;
            border: 2px solid;
            border-radius: 15px;
            margin-top: 30px;
            margin-left: 30px;
            margin-right: 30px;
            padding: 19px;
            background-color: rgb(255, 255, 255);
            box-sizing: border-box;
        }
    </style>

    <title>ScreenShot</title>
</head>

<body>
    <div id="screenshot" style="display: inline-block;width: 630px;height: 500px;">
        <div id="contentbox">
            <table>
                <tr>
                    <td>
                        <img id="avatar" src="<?php echo str_replace("_normal", "", $data->user->profile_image_url_https); ?>"></img>
                    </td>
                    <td id="userdata">
                        <?php echo $data->user->name; ?>
                        <br>
                        <span id="username">@<?php echo $data->user->screen_name; ?></span>
                    </td>
                    <td>
                       <!--  <img id="akharintweet_logo" src="img/logo_akharinkhabar.png"></img> -->
                    </td>
                </tr>
                <tr>
                    <td colspan="3">
                        <hr style="color: #D0D0D0;width: 100%;">
                    </td>
                </tr>
                <tr>
                    <td colspan="3" id="tweetext">
                        <?php
                        $remove_link = preg_replace("@(https?://([-\w\.]+[-\w])+(:\d+)?(/([\w/_\.#-]*(\?\S+)?[^\.\s])?)?)@", '', $data->full_text);
                        $rep_hashtag = preg_replace('/(?:^|\s)#([^\s]+)/', ' <a class="hashtag">#$1</a>', $remove_link);
                        $rep_mention = preg_replace('/(?:^|\s)@([^\s]+)/', ' <a class="hashtag">@$1</a>', $rep_hashtag);
                        echo str_replace("\n", "<br>", $rep_mention);
                        ?>
                    </td>
                </tr>
                <tr>
                    <td colspan="3" id="footeri">
                        <?php echo $obj->set_tweet_time($data->created_at); ?> · Twitter for AkharinTwit
                    </td>
                </tr>
            </table>
        </div>
        </br>
        </br>
    </div>
</body>

</html>