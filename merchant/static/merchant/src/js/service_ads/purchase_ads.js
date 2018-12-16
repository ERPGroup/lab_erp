var arr = new Array();
var amount;
$(document).ready(function () {
    paypal.Button.render({
        // Set your environment
        env: 'sandbox', // sandbox | production
        locale: 'en_US',
        // Specify the style of the button
        style: {
            label: 'paypal',
            //layout: 'vertical',  // horizontal | vertical
            size: 'medium', // medium | large | responsive
            shape: 'rect', // pill | rect
            color: 'gold',
            tagline: false
            //fundingicons: false,   // gold | blue | silver | white | black
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
            amount = parseFloat($('#amount').val());
            amount = (amount / 22000).toFixed(2);
            return actions.payment.create({
                payment: {
                    transactions: [{
                        amount: {
                            total: amount,
                            currency: 'USD'
                        }
                    }]
                },
                description: 'Thanh toán hợp đồng quảng cáo' + $('#select_type').val(),
                item_list: {
                    items: [{
                        name: $('#select_type').val(),
                        description: 'Brown hat.',
                        quantity: '1',
                        price: amount,
                        currency: 'USD'
                    }, ]
                }
            });
        },

        onAuthorize: function (data, actions) {
            return actions.payment.execute()
                .then(function () {
                    data_info = {
                        'inputPurchaseName': data.paymentID,
                        'inputServiceId': $('#select_type').val(),
                        'inputAmount': $('#amount').val(),
                        'inputState': 1,
                        'inputStart_date': $('#dateAvailable').val(),
                    }
                    $.ajax({
                        url: 'https://laberp.pythonanywhere.com/merchant/purchase_service_ads',
                        method: 'POST',
                        contentType: 'application/x-www-form-urlencoded',
                        data: data_info,
                        success: function (response) {
                            if (response == "Success!")
                                alert('Payment complete');
                            else {
                                alert('Error System ');
                            }
                        },
                        error: function (e) {
                            alert('Failed ');
                        }
                    })
                    window.alert('Payment Complete!');
                    console.log(data);
                });
        },
        onError: function (error) {
            // You will want to handle this differently
            alert('Lỗi hệ thống vui lòng thử lại.', +error)
        }
    }, '#paypal-button');


    $.ajax({
        url: 'https://laberp.pythonanywhere.com/merchant/getListAds/',
        type: 'GET',
        dataType: 'json',
        async: false,
        success: function (data) {
            var i = 0;
            $.each(data, function (i, item) {
                var obj = {
                    id: item.id,
                    service_name: item.service_name,
                    type_service: item.type_service,
                    position: item.position,
                    amount: item.amount,
                    day_limit: item.day_limit,
                };
                arr[i] = obj;
                i++;
            })
        }
    })
})
$('#select_type').change(function () {

    var flag = false;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].id == this.value) {
            document.getElementById('day_limit').value = arr[i].day_limit;
            document.getElementById('position').value = arr[i].position;
            document.getElementById('amount').value = arr[i].amount;
            $.ajax({
                url: 'https://laberp.pythonanywhere.com/merchant/getDateAvailable/' + arr[i].position + '&' +
                    arr[i].id,
                type: 'GET',
                dateType: 'json',
                success: function (data) {
                    var result = '';
                    $.each(data, function (i, item) {
                        result += '<option value="' + item + '">' + item + '</option>';
                    })
                    $('#dateAvailable').html('');
                    $('#dateAvailable').html(result);
                }
            });
            break;
        }
    }
});