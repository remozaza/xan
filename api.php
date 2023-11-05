
<?php
// @xancheck @xancheck @xancheck @xancheck @xancheck

require 'vendor/autoload.php'; //  autoload.php from Stripe PHP library

use Stripe\Stripe;
use Stripe\PaymentMethod;
use Stripe\StripeObject;

// sk key 
Stripe::setApiKey('your_sk');

$creditCardInfo = isset($_GET['cc']) ? $_GET['cc'] : null;

if ($creditCardInfo) {
    list($creditCardNumber, $expMonth, $expYear, $cvv) = explode('|', $creditCardInfo);

    // PaymentMethod
    $paymentMethod = PaymentMethod::create([
        'type' => 'card',
        'card' => [
            'number' => $creditCardNumber,
            'exp_month' => $expMonth,
            'exp_year' => $expYear,
            'cvc' => $cvv,
        ],
    ]);

    if ($paymentMethod instanceof StripeObject && isset($paymentMethod->id)) {
        // temporary charge of $0.01 to $0.05
        $amount = mt_rand(1, 5) / 100;
        $currency = 'usd';

        //  charge
        $charge = \Stripe\Charge::create([
            'amount' => $amount * 100, // cents
            'currency' => $currency,
            'source' => $paymentMethod->id,
        ]);

        echo "APPROVED | $creditCardNumber|$expMonth|$expYear|$cvv | API BY @xancheck";
    } else {
        echo "DECLINED | $creditCardNumber|$expMonth|$expYear|$cvv | Invalid credit card information APIBY @xancheck";
    }
} else {
    echo "Please provide credit card information using the format ?cc={creditcardnumber}|{expmonth}|{expyear}|{cvv} APIBY @xancheck";
}
