/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#c1d1c1',
        fontFamily: '"Titan One", Josefin Sans, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa775a',
        iconColor: '#fa775a'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// The handling of realtime errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-erros');
    if (event.error) {
        var html= `
            <span class="icon" role="alert">
                <i class="bi bi-x-square"></i>
            </span>
            <span>${event.error.message}</span>
            `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});