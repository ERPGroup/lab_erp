// Purchase Post


$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_service = check_url[check_url.length - 1]
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/merchant/service/' + id_service,
        method: 'GET',
        contentType: 'application/json',
        success: function(service){
            console.log(service)
            if (service == -1){
                alert('Gói tin này không tồn tại!')
                window.location.replace('/merchant/service_post')
            }

            $('.title').text(service.service_name);
            $('.amount').text(service.amount);

            var box = ''; 
            if(service.value != 0)
                box +='<li>'+ service.value +' tin đăng</li>';
            else
                box +='<li class="disable">'+ service.value +' tin đăng</li>';
            
            if(service.quantity_product != 0)
                box +='<li>'+ service.quantity_product +' sản phẩm mỗi tin</li>';
            else
                box +='<li class="disable">'+ service.quantity_product +' sản phẩm mỗi tin</li>';

            // setup day_limit
            if(service.day_limit != 0)
                box +='<li>'+ service.day_limit +' ngày sử dụng mỗi tin</li>';
            else
                box +='<li class="disable">'+ service.day_limit +' ngày sử dụng mỗi tin</li>';
            
            // setup visable_vip
            if(service.visable_vip == true)
                box +='<li>Hiển thị trên khu vực VIP</li>';
            else
                box +='<li class="disable">Không hiển thị trên khu vực VIP</li>';

            box +='<li>'+ service.usd.toFixed(2) +'$ dành cho thanh toán PayPal</li>';
            $('.pricing-content').append(box);



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
                sandbox: 'AV2N2LEhYoOJEwN2mxKLTLddeXuZOk7X5nELsm7xCq3sfn3qLS9o8ERIptw7fJDXYY3lvIl8Q1jefuAJ',
                // production: 'AX5ZfJh3e8pEhmipVMor3KMa5CxdG5a_SVNLeUhwVM9vjNo_kReF_2cdK54v9dN7Yseu1I8Y-I4BH5AZ'
                },
                payment: function (data, actions) {
                return actions.payment.create({
                    payment: {
                    transactions: [
                        {
                        amount: {
                            total: service.usd.toFixed(2),
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
                        //Save info of payment
                        data_info = {
                            'inputPurchaseName': data.paymentID,
                            'inputServiceId': id_service,
                            'inputAmount': service.usd.toFixed(2),
                            'inputState': 1,
                        }

                        $.ajax({
                            url: 'https://laberp.pythonanywhere.com/merchant/purchase_service',
                            method: 'POST',
                            contentType: 'application/x-www-form-urlencoded',
                            data: data_info,
                            success: function(response){
                                alert(response);
                            }
                        })

                    window.alert('Thanh toán hoàn tất!');
                    console.log(data);
                    });
                }
            }, '#paypal-button-container');
        },
    });
});