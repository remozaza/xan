
<?php
// @xancheck @xancheck @xancheck @xancheck @xancheck

require 'vendor/autoload.php'; //  autoload.php from Stripe PHP library

use Stripe\Stripe;
use Stripe\PaymentMethod;
use Stripe\StripeObject;

// sk key 
Stripe::setApiKey('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');

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
        // temporary charge of $0.50 to $0.99
        $amount = mt_rand(50, 99) / 100;
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
