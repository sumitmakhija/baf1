document.getElementById('complaintForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Get form values
    const customer_name = document.getElementById('customer_name').value;
    const customer_email = document.getElementById('customer_email').value;
    const customer_contact_no = document.getElementById('customer_contact_no').value;
    const customer_contact_no_landline = document.getElementById('customer_contact_no_landline').value;
    const customer_contact_acc_no = document.getElementById('customer_contact_acc_no').value;
    const customer_city = document.getElementById('customer_city').value;
    const product_detail = document.getElementById('product_detail').value;
    const complaint_detail = document.getElementById('complaint_detail').value;

    // Show spinner and hide messages initially
    document.getElementById('spinner').style.display = 'inline-block';
    document.getElementById('successMessage').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';

    // Submit the form using Axios
    axios.post('/submit-complaint-form/', {
        customer_name,
        customer_email,
        customer_contact_no,
        customer_contact_no_landline,
        customer_contact_acc_no,
        customer_city,
        product_detail,
        complaint_detail
    })
    .then(function (response) {
        if (response.data.success) {
            // Show success message
            document.getElementById('successMessage').style.display = 'block';
            document.getElementById('complaintForm').reset();
        }
        // Hide spinner
        document.getElementById('spinner').style.display = 'none';
    })
    .catch(function (error) {
        // Show error message
        document.getElementById('errorMessage').style.display = 'block';
        // Hide spinner
        document.getElementById('spinner').style.display = 'none';
    });
});

document.getElementById('fraud-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form values
    const customer_name = document.getElementById('customer_name_fraud').value;
    const customer_email = document.getElementById('email_fraud').value;
    const customer_cnic = document.getElementById('cnic').value;
    const customer_transaction_date = document.getElementById('transaction_date').value;
    const customer_transaction_amt = document.getElementById('transaction_amt').value;
    const customer_acct_amt = document.getElementById('account_amount').value;
    const customer_contact = document.getElementById('contact').value;
    const customer_remarks = document.getElementById('remarks').value;
    const complaint_detail = document.getElementById('additional_info').value;

    // Show spinner and hide messages initially
    document.getElementById('spinner-fraud').style.display = 'inline-block';
   
    // Submit the form using Axios
    axios.post('/submit-fraud-form/', {
        customer_name,
        customer_email,
        customer_cnic,
        customer_transaction_date,
        customer_transaction_amt,
        customer_acct_amt,
        customer_contact,
        customer_remarks,
        complaint_detail,
    })
    .then(function (response) {
        if (response.data.success) {
            // Show success message
            document.getElementById('successMessage-fraud').style.display = 'block';
            document.getElementById('fraud-form').reset();
        }
        // Hide spinner
        document.getElementById('spinner-fraud').style.display = 'none';
    })
    .catch(function (error) {
        // Show error message
        document.getElementById('errorMessage-fraud').style.display = 'block';
        // Hide spinner
        document.getElementById('spinner-fraud').style.display = 'none';
    });
});