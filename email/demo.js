$(document).ready(function() {
	function init() {
		$('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year
            format: 'dd/mm/yyyy',
            min: new Date()
        });
		$(".datepicker").each(function() {

            var defaultDate = $(this).prop('defaultValue');
		    if(defaultDate != ""){

                $(this).pickadate('picker').set('select', defaultDate);
		    }
		});
	}

	init();
		$.LoadingOverlay("show");
    function couponValidator(coupon_validity) {
        $('#show-progress').addClass('hidden-div');
        if(coupon_validity) {
            var prefix = $('#promotion-prefix').val();
            var startingFrom = $('#starting-from').val();
            var noOfCodes = $('#no-of-codes').val();
            var autoPick = $('#auto-pick').prop( "checked" );
            var random = $('#random').prop( "checked" );
            $('#err-div').text('');
            $('#download-excel').removeClass('disabled');
            $('#done-progress').removeClass('hidden-div');
            $.ajax({
                type: 'GET',
                url: '/bungee/promotions/get-sample-promo/',
                data : {prefix:prefix, starting_from:startingFrom, no_of_codes:noOfCodes, auto_pick:autoPick, random:random},
                success: function(response) {
                    $('#sample-promo-code').html(response['codes'][0]);
                    $("#generated-codes").val(response['codes']);
                }
            });
        } else {
            $('#download-excel').addClass('disabled');
            $('#err-div').text('Invalid coupon configuration');
        }
    };

    function getActivePromotions(coupon_validity) {
        $.ajax({
            type: 'GET',
            url: '/bungee/promotions/get-active-promotions',
            success: function(response) {
                $('#campaign-details').html(response);
								$.LoadingOverlay("hide");
            },
						error: function(response) {
							$.LoadingOverlay("hide");
						}
        });
     }

    function isNumeric(n) {
      return !isNaN(parseFloat(n)) && isFinite(n);
    }

    function disableProgressBar() {
        $('#download-excel').removeClass('disabled');
    }

    function addPrefix(prefix, sample_promo_code){

        if(prefix.length != 0){
            sample_promo_code =
                    prefix +
                    sample_promo_code.substr(prefix.length, sample_promo_code.length-1);
        }
        return sample_promo_code;
    }

    function addSuffix(suffix, sample_promo_code){

        if(suffix.length != 0){
            sample_promo_code =
                    sample_promo_code.substr(0, sample_promo_code.length - suffix.length) +
                    suffix

        }
        return sample_promo_code;
    }

    function changeCouponCode(event, defaultPromoCode){
        if($('#sample-promo-code').html()=="Coupon Code"){

                $('#sample-promo-code').html(defaultPromoCode);
            }

        var prefix = $('#promotion-prefix').val();
        var startingFrom = $('#starting-from').val();
        var sample_promo_code = $('#sample-promo-code').html();
        var coupon_code_length = prefix.length+startingFrom.length;

        if(coupon_code_length>=6){

            sample_promo_code = prefix + startingFrom;
        } else{

            sample_promo_code = defaultPromoCode;
            sample_promo_code = addPrefix(prefix, sample_promo_code);
            sample_promo_code = addSuffix(startingFrom, sample_promo_code);
        }

        if(sample_promo_code.length>11){

            $('#sample-promo-code').html(
                sample_promo_code.substr(0, 11) +
                " " +
                sample_promo_code.substr(11, sample_promo_code.length)
            );
        } else{
            $('#sample-promo-code').html(sample_promo_code);
        }
    }

    function filterPromotions(){
        var expiredPromotionElements = $('input[name=expired-promo]');
        if(expiredPromotionElements.length > 0){

            if (expiredPromotionElements[0].checked){

                $.ajax({
                    type: 'GET',
                    url: '/bungee/promotions/get-expired-promotions',
                    success: function(response) {
                        $('#campaign-details').html(response);
                    }
                });
            }else{

                getActivePromotions();
            }
        }
        else{
            getActivePromotions();
        }
    }

    $('select').material_select();

    var googleAnalyticsFunction = function(context){
        var pathName = window.location.pathname;
        ga('send', 'event', context, pathName);
     };

    $('#configure-promotion-form').on( "click", "#generate-codes", function( event ) {
        event.preventDefault();

        var prefix = $('#promotion-prefix').val();
        var startingFrom = $('#starting-from').val();
        var noOfCodes = $('#no-of-codes').val();
        var autoPick = $('#auto-pick').prop( "checked" );
        var random = $('#random').prop( "checked" );
        var sequential = $('#sequential').prop( "checked" );
        var lastCode = parseInt(startingFrom) + parseInt(noOfCodes) - 1;
        var lastCodeLen = lastCode.toString().length;
        var leadingZeroes = startingFrom.length - lastCodeLen;

        if (random && !isNumeric(noOfCodes)) {
            $('#err-div').text("Please Numeric values in Number of codes field");
            $('#show-progress').addClass('hidden-div');
            $('#done-progress').addClass('hidden-div');
            $('#download-excel').addClass('disabled');
            return;
        }
        if (random && noOfCodes === "") {
            $('#err-div').text("Please fill the fields required for creating promotions");
            $('#show-progress').addClass('hidden-div');
            $('#done-progress').addClass('hidden-div');
            $('#download-excel').addClass('disabled');
            return;
        }

        if (sequential && !isNumeric(startingFrom) && !isNumeric(noOfCodes)) {
            $('#err-div').text("Please Numeric values in Starting number and Number of codes field");
            $('#show-progress').addClass('hidden-div');
            $('#done-progress').addClass('hidden-div');
            $('#download-excel').addClass('disabled');
            return;
        }
        if (sequential && !autoPick && startingFrom === "" || noOfCodes === "") {
            $('#err-div').text("Please fill the fields required for creating promotions");
            $('#show-progress').addClass('hidden-div');
            $('#done-progress').addClass('hidden-div');
            $('#download-excel').addClass('disabled');
            return;
        }
        if (sequential && !autoPick && startingFrom === "") {
            $('#err-div').text("Either enter a starting number or select auto pick");
            $('#show-progress').addClass('hidden-div');
            $('#done-progress').addClass('hidden-div');
            $('#download-excel').addClass('disabled');
            return;
        }
        var payload = {'prefix': prefix, 'starting_from': startingFrom, 'no_of_codes': noOfCodes, 'auto_pick': autoPick,
        		'random': random};
        $('#show-progress').removeClass('hidden-div');
        $('#done-progress').addClass('hidden-div');
        client('/bungee/validate/promotion-code/', 'POST', payload, couponValidator);

        if(autoPick){
            googleAnalyticsFunction('Auto-picking-promotion-codes-for-new-promotion');
        }
        googleAnalyticsFunction('Generated-promotion-codes-for-new-promotion');
    });

    $('#configure-promotion-form').on( "click", "#auto-pick", function( event ) {
        $("#starting-from").prop('disabled', ! $("#starting-from").prop('disabled') );
    });

    $('#configure-promotion-form').on( "click", "#publish-promotion", function( event ) {
        event.preventDefault();
        googleAnalyticsFunction('Publish-new-promotion-button');
        $("#publish-promotion-form").validate({
            rules: {
                "auto-pick": { required: false },
                "campaign-name": { required: true },
                "campaign-constraint-type": { required: true, select_values_except: "default-selected-option", },
                "constraint-value": { required: true, number: true, min: 0, },
                "discount-value": { required: true, number: true, min: 0 },
                "end-date": {    required: function(element){
                                    return !$('#no-expiry').is(':checked');
                                    },
                            },
                "generate-code": { required: true },
                "no-expiry": {   required: false,
                                normalizer: function(element){
                                        return $('#no-expiry').is(':checked').toString();
                                    },
                             },
                "promotion-scheme": { required: true },
                "promotion-vehicle": {  required: true,
                                        select_values_except: "default-selected-option",
                                    },
                "promotion-prefix": { required: function(element){
                                            return  $("input[name=generate-code]:checked").val() != "random";
                                            },
                                    },
                "promotion-start-code": { required: function(element){
                                            return  $("input[name=generate-code]:checked").val() != "random" &&
                                                    !$('#auto-pick').is(':checked');
                                            },
                                    },
                "promotion-number": { required: true, min: 1 },
                "promotion-type": { required: true,
                                    select_values_except: "default-selected-option",
                                },
                "start-date": { required: true },
            },
            messages:{
                "discount-value": {min: "Please enter a value greater than {0}",},
                "constraint-value": {min: "Please enter a value greater than {0}",}
            },
            errorPlacement: function(error, element) {
                if ( element.is(":radio") ) {
                    error.appendTo(element.parent());
                } else { // This is the default behavior
                    error.insertAfter(element);
                }
            },
        });
        if(!$("#publish-promotion-form").valid()) {
            return;
        }
        $.ajax({
            type: 'POST',
            url: '/bungee/promotions/publish-new-promotion',
            data : $('#publish-promotion-form').serialize(),
            success: function(response) {
                $('#new-promotion-modal').html(response);
                $('#new-promotion-modal').modal({
                dismissible:false});
                $('#new-promotion-modal').modal('open');
                $('#publish-promotion').prop('disabled', true);
            }
        });
    })

    $('#configure-promotion-form').on( "click", "#download-excel", function( event ) {
        event.preventDefault();
        var prefix = $('#promotion-prefix').val();
        var startingFrom = $('#starting-from').val();
        var noOfCodes = $('#no-of-codes').val();
        var random = $('#random').prop( "checked" );
        var autoPick = false;
        var codes = $("#generated-codes").val();
        if ($('#auto-pick').prop( "checked" )) {
            autoPick = true;
        };
        var url = '/bungee/promotions/download-as-xls?prefix='+prefix+"&starting_from="+startingFrom+"&no_of_codes="+noOfCodes+"&auto_pick="+autoPick+"&random="+random+"&codes="+codes;
        window.open(url);
        googleAnalyticsFunction('Downloading-generated-promotion-codes');
    });

    $('#configure-promotion-form').on( "change", "#promotion-vehicle", function( event ) {
        $('#selected-vehicle').html($('#promotion-vehicle').val());
    });

    $('#configure-promotion-form').on("input", "#promotion-prefix", {}, function(event){

       changeCouponCode(event, '000000');
    });

    $('#configure-promotion-form').on("input", "#starting-from", {}, function(event){

       changeCouponCode(event, '000000');
    });

    $('#configure-promotion-form').on("click", "#auto-pick", {}, function(event){

        $('#starting-from').val('');
        changeCouponCode(event, 'XXXXXX');
    });

    $('#configure-promotion-form').on("change", "#random", {}, function(event){
    	$('.select-prefix-row').hide();
    	$('.select-start-no-row').hide();
     });

    $('#configure-promotion-form').on("change", "#sequential", {}, function(event){
    	$('.select-prefix-row').show();
    	$('.select-start-no-row').show();
     });

    $('#configure-promotion-form, #update-promotion-form').on("change", "#no-expiry", {}, function(event){

    	if ($('#no-expiry').is(':checked')){

    	    $("#end-date").prop('disabled', true);
    	}else{
    	    $("#end-date").prop('disabled', false);
    	}
     });

    $('#configure-promotion-form').on( "change", "#start-date", function(event) {

        var fullDate = new Date();
        var twoDigitMonth = (fullDate.getMonth() + 1).toString().paddingLeft("00")
        var twoDigitDate = fullDate.getDate().toString().paddingLeft("00");
        var currentDate = [twoDigitDate, twoDigitMonth, fullDate.getFullYear()].join("/");

        if($("#start-date").val()==currentDate){
            $("#start-date-error").hide();
            $(".today-effectiveness").show();
        }else{
            $(".today-effectiveness").hide();
        }
     });

    $('input[name=expired-promo]').change(function(event){
        filterPromotions();
    });

    filterPromotions();

    String.prototype.paddingLeft = function(paddingValue) {
      return String(paddingValue + this).slice(-paddingValue.length);
    }

    $(document).on("click", "#edit-download-excel", function(e){
        var url = '/bungee/promotions/' + $(e.target).data("id") + '/download-as-xls';
        window.open(url);
        googleAnalyticsFunction('Downloading-promotion-codes-from-edit');
    });

    $('#promotion-scheme').change(function(event){
        var scheme = $(this).val();
        googleAnalyticsFunction('Selected-promotion-scheme');
        $.ajax({
            type: 'GET',
            url: '/bungee/promotions/get-configuration-form',
            data : {'scheme': scheme},
            success: function(response) {
                $('#configure-promotion-form').html(response);
                $('.collapsible').collapsible();
                    $('ul.tabs').tabs();
                    $('select').material_select();
                    $('.datepicker').pickadate({
                        selectMonths: true, // Creates a dropdown to control month
                        selectYears: 15, // Creates a dropdown of 15 years to control year
                        format: 'dd/mm/yyyy',
                        min: new Date(),
                        default: 'today',
                    });
            }
        });
    })

    $(document).on('click', "#update-promotion", function(e) {
    	var promotionId = $(this).val();
        event.preventDefault();

        $("#update-promotion-form").validate({
            rules: {
                "promotion-end-date": { required: function(element){
                                            return !$('#no-expiry').is(':checked');
                                        },
                            },
                "no-expiry": {  required: false,
                                normalizer: function(element){
                                        return $('#no-expiry').is(':checked').toString();
                                    },
                             },
                "promotion-start-date": { required: true },
            },
            errorPlacement: function(error, element) {
                if ( element.is(":radio") ) {
                    error.appendTo(element.parent());
                } else { // This is the default behavior
                    error.insertAfter(element);
                }
            },
        });


        if(!$("#update-promotion-form").valid()) {
            return;
        }
        $.ajax({
            type: 'POST',
            url: '/bungee/promotions/edit-promotions/' + promotionId + "/",
            data : $('#update-promotion-form').serialize(),
            success: function(response) {
                $('#new-promotion-modal').html(response);
                if($('span#error').text() != '') {
                	$('#new-promotion-modal').modal({
                        dismissible:false});
                    $('#new-promotion-modal').modal('open');
                }
                else {
                  window.location = "/bungee/promotions/home/";
                }
            }
        });
    })
});
