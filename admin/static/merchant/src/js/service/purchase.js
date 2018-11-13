// Purchase Post
$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_service = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://localhost:8000/merchant/service/' + id_service,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            service = response[0]['fields']
            // Render the PayPal button
            paypal.Button.render({
                // Set your environment
                env: 'sandbox', // sandbox | production
                
                // Specify the style of the button
                style: {
                layout: 'vertical',  // horizontal | vertical
                size:   'responsive',    // medium | large | responsive
                shape:  'pill',      // pill | rect
                color:  'gold',      // gold | blue | silver | white | black
                },
                
                // Specify allowed and disallowed funding sources
                //
                // Options:
                // - paypal.FUNDING.CARD
                // - paypal.FUNDING.CREDIT
                // - paypal.FUNDING.ELV
                // funding: {
                //   allowed: [
                //     paypal.FUNDING.CARD,
                //     paypal.FUNDING.CREDIT
                //   ],
                //   disallowed: []
                // },
                
                // PayPal Client IDs - replace with your own
                // Create a PayPal app: https://developer.paypal.com/developer/applications/create
                client: {
                sandbox: 'AX5ZfJh3e8pEhmipVMor3KMa5CxdG5a_SVNLeUhwVM9vjNo_kReF_2cdK54v9dN7Yseu1I8Y-I4BH5AZ',
                // production: 'AX5ZfJh3e8pEhmipVMor3KMa5CxdG5a_SVNLeUhwVM9vjNo_kReF_2cdK54v9dN7Yseu1I8Y-I4BH5AZ'
                },
                payment: function (data, actions) {
                return actions.payment.create({
                    payment: {
                    transactions: [
                        {
                        amount: {
                            total: service.amount,
                            currency: 'USD'
                        }
                        }
                    ]
                    }
                });
                },
                
                onAuthorize: function (data, actions) {
                return actions.payment.execute()
                    .then(function () {
                        data_info = {
                            'inputPurchaseName': data.paymentID,
                            'inputServiceId': id_service,
                            'inputAmount': service.amount,
                            'inputState': 1,
                        }
                        $.ajax({
                            url: 'http://localhost:8000/merchant/purchase_service',
                            method: 'POST',
                            contentType: 'application/x-www-form-urlencoded',
                            data: data_info,
                            success: function(response){

                            }
                        })
                    window.alert('Payment Complete!');
                    console.log(data);
                    });
                }
            }, '#paypal-button-container');
        },
    });
});