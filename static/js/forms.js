/***************************************************************
 * Complaint form Contact us 
 ***************************************************************/ 

$(document).ready(function() {
    // Initialize input masking
    $('#customer_contact_no').mask('0000-0000000', { placeholder: '03XX-XXXXXXX' });
    $('#customer_contact_no_landline').mask('(000)-00000000', { placeholder: '(XXX)-XXXXXXXX' });
    // $('#customer_contact_acc_no').mask('00000000000000000000', { placeholder: 'Enter your Account Number' });


    $.validator.addMethod("lettersOnly", function (value, element) {
        // Allow letters and spaces
        return this.optional(element) || /^[a-zA-Z\s]+$/.test(value);
    }, "Only alphabets and spaces are allowed.");

    // Custom rule for alphanumeric, underscores, hyphens, and spaces
    $.validator.addMethod("alphaNumeric", function (value, element) {
        // Allow letters, numbers, underscores, hyphens, and spaces
        return this.optional(element) || /^[a-zA-Z0-9_-\s]+$/.test(value);
    }, "Only alphabets, numbers, underscores, hyphens, and spaces are allowed.");


    // Initialize form validation
    $("#complaintForm").validate({
        rules: {
            customer_name: {
                required: true,
                lettersOnly: true,
                maxlength: 100
            },
            customer_contact_no: {
                required: true,
                // minlength: 12, // 03XX-XXXXXXX (11 digits + 1 hyphen)
                // maxlength: 12
            },
            customer_contact_acc_no: {
                required: true,
                digits: true,
                maxlength: 20
            },
            customer_email: {
                required: true,
                email: true
            },
            customer_contact_no_landline: {
                minlength: 14, // (XXX)-XXXXXXXX (14 characters)
                maxlength: 14
            },
            customer_city: {
                maxlength: 100,
                alphaNumeric:true,
            },
            product_detail: {
                alphaNumeric: true,
                maxlength: 200,
            },
            complaint_detail: {
                required: true,
                alphaNumeric: true,
                maxlength: 255
            }
        },
        messages: {
            customer_name: {
                required: "Please enter your name",
                maxlength: "Name must be less than 100 characters"
            },
            customer_contact_no: {
                required: "Please enter your mobile number",
                minlength: "Mobile number must be in the format 03XX-XXXXXXX",
                maxlength: "Mobile number must be in the format 03XX-XXXXXXX"
            },
            customer_contact_acc_no: {
                required: "Please enter your account number",
                digits: "Please enter only digits",
                maxlength: "Account number must be less than 20 digits"
            },
            customer_email: {
                required: "Please enter your email address",
                email: "Please enter a valid email address"
            },
            customer_contact_no_landline: {
                minlength: "Landline number must be in the format (XXX)-XXXXXXXX",
                maxlength: "Landline number must be in the format (XXX)-XXXXXXXX"
            },
            customer_city: {
                maxlength: "City name must be less than 100 characters"
            },
            product_detail: {
                maxlength: "Product detail must be less than 200 characters"
            },
            complaint_detail: {
                required: "Please enter your complaint details",
                maxlength: "Complaint detail must be less than 255 characters"
            }
        },
        submitHandler: function(form) {
            $('#spinner').show(); // Show spinner

            // Get CSRF token from the cookie (or from a meta tag if preferred)
            const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
            // Get form data
            const formData = {
                customer_name: $('#customer_name').val(),
                customer_email: $('#customer_email').val(),
                customer_contact_no: $('#customer_contact_no').val(),
                customer_contact_no_landline: $('#customer_contact_no_landline').val(),
                customer_contact_acc_no: $('#customer_contact_acc_no').val(),
                customer_city: $('#customer_city').val(),
                product_detail: $('#product_detail').val(),
                complaint_detail: $('#complaint_detail').val()
            };

            // console.log("csrf token", csrf_token);
            // console.log("form entries: ", formData);
            // debugger;

            // Submit the form using Axios
            axios.post('/submit-complaint-form/', formData, {
                headers: {
                    'X-CSRFToken': csrf_token // Include CSRF token in headers
                }
            })
            .then(function(response) {
                if (response.data.success) {
                    // Show success message
                    setTimeout(function() {
                        $('#spinner').hide(); // Hide spinner
                        Toastify({
                            text: "Form submitted successfully!",
                            duration: 3000,
                            close: true,
                            gravity: "top",
                            position: "right",
                            backgroundColor: "#28a745",
                        }).showToast();
                        form.reset(); // Reset form
                    }, 2000);
                }
            })
                .catch(function (error) {
                // console.log("error on axios: ", error);
                // Show error message
                Toastify({
                    text: error,
                    duration: 3000,
                    close: true,
                    gravity: "top",
                    position: "right",
                    backgroundColor: "#dc3545",
                }).showToast();
                // Hide spinner
                $('#spinner').hide();
            });

            
        },
        invalidHandler: function(event, validator) {
            Toastify({
                text: "Please fill out all required fields correctly.",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "right",
                backgroundColor: "#dc3545",
            }).showToast();
        }
    });
});


/***************************************************************
 * fraud form Contact us - modal based
 ***************************************************************/ 

$(document).ready(function() {
    // Input masking
    $('#cnic').mask('00000-0000000-0', { placeholder: 'XXXXX-XXXXXXX-X' }); // CNIC masking
    $('#contact').mask('0000-0000000', { placeholder: '03XX-XXXXXXX' }); // Contact masking

    // Add custom validation methods
    // $.validator.addMethod("cnicFormat", function(value, element) {
    //     // CNIC format: XXXXX-XXXXXXX-X
    //     return this.optional(element) || /^\d{5}-\d{7}-\d{1}$/.test(value);
    // }, "Please enter a valid CNIC No (XXXXX-XXXXXXX-X).");

    // $.validator.addMethod("contactFormat", function(value, element) {
    //     // Contact format: 03XX-XXXXXXX
    //     return this.optional(element) || /^03\d{2}-\d{7}$/.test(value);
    // }, "Please enter a valid Contact No (03XX-XXXXXXX).");

    $.validator.addMethod("numericOnly", function(value, element) {
        // Numeric only
        return this.optional(element) || /^\d+$/.test(value);
    }, "Please enter only numbers.");

    $.validator.addMethod("lettersOnly", function (value, element) {
        // Allow letters and spaces
        return this.optional(element) || /^[a-zA-Z\s]+$/.test(value);
    }, "Only alphabets and spaces are allowed.");

    // Custom rule for alphanumeric, underscores, hyphens, and spaces
    $.validator.addMethod("alphaNumeric", function (value, element) {
        // Allow letters, numbers, underscores, hyphens, and spaces
        return this.optional(element) || /^[a-zA-Z0-9_-\s]+$/.test(value);
    }, "Only alphabets, numbers, underscores, hyphens, and spaces are allowed.");



    // Initialize form validation
    $("#fraud-form").validate({
        rules: {
            customer_name_fraud: {
                required: true,
                lettersOnly: true
            },
            cnic: {
                required: true,
                // cnicFormat: true
            },
            transaction_amt: {
                numericOnly: true
            },
            contact: {
                // contactFormat: true
            },
            remarks: {
                maxlength: 200,
                alphaNumeric: true,
            },
            email_fraud: {
                required: true,
                email: true
            },
            additional_info: {
                alphaNumeric: true,
                maxlength: 255,
            }
        },
        messages: {
            customer_name_fraud: {
                required: "Please enter your name.",
                lettersOnly: "Only alphabets and spaces are allowed.",
                maxlength: "Complaint detail must be less than 255 characters"
            },
            cnic: {
                required: "Please enter your CNIC No.",
                // cnicFormat: "Please enter a valid CNIC No (XXXXX-XXXXXXX-X)."
            },
            transaction_amt: {
                numericOnly: "Please enter only numbers."
            },
            contact: {
                contactFormat: "Please enter a valid Contact No (03XX-XXXXXXX)."
            },
            remarks: {
                maxlength: "remarks must be less than 255 characters"
            },
            email_fraud: {
                required: "Please enter your email address.",
                email: "Please enter a valid email address."
            },
            additional_info: {
                alphaNumeric: true,
                maxlength: "additional info must be less than 255 characters",
            }
        },
        submitHandler: function(form) {
            $("#spinner-fraud").show(); // Show spinner

            // Get form data
            const formData = {
                customer_name: $("#customer_name_fraud").val(),
                customer_email: $("#email_fraud").val(),
                customer_cnic: $("#cnic").val(),
                customer_transaction_date: $("#transaction_date").val(),
                customer_transaction_amt: $("#transaction_amt").val(),
                customer_contact: $("#contact").val(),
                customer_acct_amt: $("#account_amount").val(),
                customer_remarks: $("#remarks").val(),
                complaint_detail: $("#additional_info").val()
            };

            // Get CSRF token
            const csrf_token = $('[name=csrfmiddlewaretoken]').val();

            // console.log("formData fraud: ", formData);
            // debugger;

            // Send Axios POST request
            axios.post('/submit-fraud-form/', formData, {
                headers: {
                    'X-CSRFToken': csrf_token // Include CSRF token in headers
                }
            })
            .then(response => {
                $("#spinner-fraud").hide(); // Hide spinner
                // console.error(response);
                Toastify({
                    text: "Form submitted successfully!",
                    duration: 3000,
                    close: true,
                    gravity: "top",
                    position: "right",
                    backgroundColor: "#28a745",
                }).showToast();
                form.reset(); // Reset form
            })
            .catch(error => {
                $("#spinner-fraud").hide(); // Hide spinner
                console.log("fraud form error axios: ", error);
                Toastify({
                    text: "An error occurred. Please try again.",
                    duration: 3000,
                    close: true,
                    gravity: "top",
                    position: "right",
                    backgroundColor: "#dc3545",
                }).showToast();
                // console.error(error);
            });
        }
    });
});

/***************************************************************
 * cookie to fetch csrf token
 ***************************************************************/ 
// Function to get CSRF token from the cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
