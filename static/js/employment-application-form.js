/****************************************************
 * Employment application form javascript handling
 ****************************************************/

$(document).ready(function () {
    /**
     * File input handling
     * */ 
    // Handle file input display
    document.getElementById('cv_file').addEventListener('change', function (e) {
        const fileName = e.target.files[0]?.name; // Get the selected file name
        if (fileName) {
            const uploadInstructions = this.parentElement.querySelector('.upload-instructions');
            uploadInstructions.textContent = fileName; // Update the file name display
        }
    });

    /**
     * form validation functions
     * */

    // Function to validate name (string only, no numbers or special characters)
    function validateName(name) {
        const regex = /^[A-Za-z\s]+$/; // Allows letters and spaces only
        return regex.test(name);
    }

    // Function to validate address (alphanumeric and special characters such as # , . - /)
    function validateAddress(address) {
        const regex = /^[A-Za-z0-9\s#,.-\/]+$/; // Allows alphanumeric, spaces, and specific special characters
        return regex.test(address);
    }

    // Function to validate institution (alphanumeric)
    function validateInstitution(institution) {
        const regex = /^[A-Za-z0-9\s]+$/; // Allows alphanumeric and spaces
        return regex.test(institution);
    }

    // Function to validate additional certification (alphanumeric)
    function validateAdditionalCertification(certification) {
        const regex = /^[A-Za-z0-9\s]+$/; // Allows alphanumeric and spaces
        return regex.test(certification);
    }

    // Function to validate designation (alphanumeric)
    function validateDesignation(designation) {
        const regex = /^[A-Za-z0-9\s]+$/; // Allows alphanumeric and spaces
        return regex.test(designation);
    }

    // Function to validate organization (alphanumeric)
    function validateOrganization(organization) {
        const regex = /^[A-Za-z0-9\s]+$/; // Allows alphanumeric and spaces
        return regex.test(organization);
    }

    /**
     *  file validation
     * */ 

    // Add custom validation method for file size
    $.validator.addMethod("filesize", function (value, element, param) {
        // Check if a file is selected and its size is within the limit
        return this.optional(element) || (element.files[0] && element.files[0].size <= param);
    }, "File size must be less than {0} bytes.");

    /**
     *  input Masking - phone, emergency form and cnic
     * */ 

     // Apply mask to mobile number and emergency number fields
    $('input[name="mobile_number"]').mask('0000-0000000', {
        placeholder: '03XX-XXXXXXX', // Placeholder text
        clearIfNotMatch: true, // Clear the field if the input doesn't match the mask
    });

    $('input[name="emergency_number"]').mask('0000-0000000', {
        placeholder: '03XX-XXXXXXX', // Placeholder text
        clearIfNotMatch: true, // Clear the field if the input doesn't match the mask
    });
    
    $('input[name="cnic"]').mask('00000-0000000-0', {
        placeholder: 'XXXXX-XXXXXXX-X', // Placeholder text
        clearIfNotMatch: true, // Clear the field if the input doesn't match the mask
    });

    /**
     * form validation
     * */
    
    // Add custom validation rules
    $.validator.addMethod("validateName", function (value, element) {
        return this.optional(element) || validateName(value);
    }, "Please enter a valid name (letters and spaces only).");

    $.validator.addMethod("validateAddress", function (value, element) {
        return this.optional(element) || validateAddress(value);
    }, "Please enter a valid address (alphanumeric and special characters such as # , . - /).");

    $.validator.addMethod("validateInstitution", function (value, element) {
        return this.optional(element) || validateInstitution(value);
    }, "Please enter a valid institution name (alphanumeric only).");

    $.validator.addMethod("validateAdditionalCertification", function (value, element) {
        return this.optional(element) || validateAdditionalCertification(value);
    }, "Please enter a valid certification (alphanumeric only).");

    $.validator.addMethod("validateDesignation", function (value, element) {
        return this.optional(element) || validateDesignation(value);
    }, "Please enter a valid designation (alphanumeric only).");

    $.validator.addMethod("validateOrganization", function (value, element) {
        return this.optional(element) || validateOrganization(value);
    }, "Please enter a valid organization name (alphanumeric only).");
    
    // Initialize form validation
    $("#employmentForm").validate({
        rules: {
            // Static fields validation rules
            full_name: {
                required: true,
                maxlength: 100,
                validateName: true, // Custom rule for name validation
            },
            email: {
                required: true,
                email: true,
            },
            mobile_number: {
                required: true,
                // digits: true,
                // pattern: /^03\d{2}-\d{7}$/, // Regex to match 03XX-XXXXXXX
            },
            emergency_number: {
                required: true,
                // digits: true,
                // pattern: /^03\d{2}-\d{7}$/, // Regex to match 03XX-XXXXXXX
            },
            cnic: {
                required: true,
                // pattern: /^\d{5}-\d{7}-\d{1}$/, // CNIC format: xxxxx-xxxxxxx-x
            },
            date_of_birth: "required",
            address: {
                required: true,
                maxlength: 255,
                validateAddress: true, // Custom rule for address validation
            },
            city: "required",
             cv_file: {
                required: true,
                accept: "application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document", // Allow PDF and Word files
                filesize: 5 * 1024 * 1024, // Max file size: 5MB
            },
        },
        messages: {
            // Static fields validation messages
            full_name: {
                required: "Please enter your full name",
                 maxlength: "Full name must be less than 100 characters.",
            },
            email: {
                required: "Please enter your email address",
                email: "Please enter a valid email address",
            },
            mobile_number: {
                required: "Please enter your mobile number",
                // pattern: "Please enter a valid mobile number in the format 03XX-XXXXXXX",
            },
            emergency_number: {
                required: "Please enter your emergency contact number",
                // pattern: "Please enter a valid emergency number in the format 03XX-XXXXXXX",
            },
            cnic: {
                required: "Please enter your CNIC",
                pattern: "CNIC must be in the format xxxxx-xxxxxxx-x",
            },
            date_of_birth: "Please enter your date of birth",
            address: {
                required: "Please enter your address",
                maxlength: "Address must be less than 255 characters.",
            },
            city: "Please select your preferred city",
            cv_file: {
                required: "Please upload your CV.",
                accept: "Only PDF and Word documents are allowed.",
                filesize: "File size must be less than 5MB.",
            },
        },
         submitHandler: async function (form) {
            // Prevent the default form submission
            event.preventDefault();

            // Show the loader overlay
            const loaderOverlay = document.getElementById('loaderOverlay');
            loaderOverlay.style.display = 'flex';

            try {
                // Create a FormData object from the form
                const formData = new FormData(form);
                const formObject = {};

                // Log all filled fields to the console
                console.log('Filled Fields:');
                formData.forEach((value, key) => {
                    console.log(`${key}: ${value}`); // Log each field and its value
                    if (key !== 'cv_file') {
                        if (key.includes('education_in_process') || key.includes('job_tenure_in_process')) {
                            formObject[key] = value === 'on'; // Convert checkbox value to boolean
                        } else {
                            formObject[key] = value; // Add other fields to the formObject
                        }
                    }
                });

                // Validate the file
                const cvFile = formData.get('cv_file');
                if (!cvFile || cvFile.size === 0) {
                    throw new Error("Please upload your CV.");
                }

                // Check file type
                const allowedTypes = [
                    "application/pdf",
                    "application/msword",
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                ];
                if (!allowedTypes.includes(cvFile.type)) {
                    throw new Error("Only PDF and Word documents are allowed.");
                }

                // Check file size (max 5MB)
                const maxSize = 5 * 1024 * 1024; // 5MB
                if (cvFile.size > maxSize) {
                    throw new Error("File size must be less than 5MB.");
                }

                // Create a new FormData object for the final submission
                const finalFormData = new FormData();
                finalFormData.append('data', JSON.stringify(formObject)); // Append form data as JSON
                finalFormData.append('cv_file', cvFile); // Append the CV file

                // Submit the form data using axios
                const response = await axios.post('/submit-employment-application/', finalFormData, {
                    headers: {
                        'Content-Type': 'multipart/form-data', // Set content type for file upload
                    },
                });

                console.log("response: ", response);

                // Handle the response
                if (response.data.status === 'success') {
                    Toastify({
                        text: "Application submitted successfully!",
                        duration: 3000,
                        close: true,
                        gravity: "top",
                        position: "right",
                        style: {
                            background: "#4CAF50", // Green color for success
                        },
                    }).showToast();
                    form.reset(); // Reset the form after successful submission
                } else {
                    throw new Error("Error submitting application. Please try again.");
                }
            } catch (error) {
                console.error('Error:', error); // Log the error to the console
                Toastify({
                    text: error.message,
                    duration: 3000,
                    close: true,
                    gravity: "top",
                    position: "right",
                    style: {
                        background: "#FF0000", // Red color for errors
                    },
                }).showToast();
            } finally {
                loaderOverlay.style.display = 'none'; // Hide the loader overlay
            }
        },
    });

    // Function to add validation rules for dynamic fields
    function addDynamicValidationRules(groupPrefix, index, customRules = {}) {
        // Add rules for select fields
        $(`select[name="${groupPrefix}[${index}]"]`).rules("add", {
            required: true,
            messages: {
                required: "This field is required",
            },
        });

        // Add rules for input fields
        $(`input[name="${groupPrefix}[${index}]"]`).rules("add", {
            required: true,
            ...customRules, // Merge custom rules if provided
            messages: {
                required: "This field is required",
                ...customRules.messages, // Merge custom messages if provided
            },
        });

        // Add rules for date fields
        $(`input[type="date"][name="${groupPrefix}[${index}]"]`).rules("add", {
            required: true,
            messages: {
                required: "This field is required",
            },
        });
    }

    // Replicate Education
    var max_fields = 8; // Maximum input boxes allowed
    var educationWrapper = $("#form-replicate-education"); // Fields wrapper
    var addEducationButton = $("#add-education"); // Add button ID
    var educationCounter = 1; // Initial text box count

    function addEducationForm(x) {
        const html = `
            <div class="form-replicate position-relative" id="form-replicate-education-${x}">
                <hr/>
                <a href="#" class="remove-form-group" data-id="${x}">
                    <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M6 5H18M9 5V5C10.5769 3.16026 13.4231 3.16026 15 5V5M9 20H15C16.1046 20 17 19.1046 17 18V9C17 8.44772 16.5523 8 16 8H8C7.44772 8 7 8.44772 7 9V18C7 19.1046 7.89543 20 9 20Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </a>
                <div class="row align-items-top">
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Last/current qualification</label>
                            <select name="qualification[${x}]" class="form-select" required>
                                <option value="" hidden="" selected="">Enter your latest qualification</option>
                                <option value="Bachelors">Bachelors</option>
                                <option value="Masters">Masters</option>
                                <option value="PhD">PhD</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Institution</label>
                            <input type="text" name="institution[${x}]" class="form-control" placeholder="Enter your institution" maxlength="100" required>
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Additional certification</label>
                            <input type="text" name="additional_certification[${x}]" class="form-control" placeholder="Enter any additional certifications" maxlength="100">
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Start date</label>
                            <input type="date" name="education_start_date[${x}]" min="1980-03-15" max="2030-12-31" class="form-control"  required>
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">End date</label>
                            <input type="date" name="education_end_date[${x}]" min="1980-03-15" max="2030-12-31" class="form-control">
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3 align-self-end">
                        <label class="form-label">
                            <input type="checkbox" name="education_in_process[${x}]"> In process
                        </label>
                    </div>
                </div>
            </div>
        `;

        $(educationWrapper).append(html); // Append the dynamic HTML to the wrapper

        // Add validation rules for the new group
        addDynamicValidationRules("qualification", x);
        addDynamicValidationRules("institution", x, {
            validateInstitution: true, // Custom rule for institution
            maxlength: 100,
            messages: {
                validateInstitution: "Please enter a valid institution name (alphanumeric only).",
                maxlength: "Institution name must be less than 100 characters.",
            },
        });
        addDynamicValidationRules("additional_certification", x, {
            validateAdditionalCertification: true, // Custom rule for institution
            maxlength: 100,
            messages: {
                validateAdditionalCertification: "Please enter a valid certification (alphanumeric only).",
                maxlength: "Certification name must be less than 100 characters.",
            },
        });
        addDynamicValidationRules("education_start_date", x);
    }

    $(addEducationButton).click(function (e) {
        e.preventDefault();
        if (educationCounter < max_fields) {
            educationCounter++;
            addEducationForm(educationCounter);
        } else {
            Toastify({
                text: "Max 8 education information allowed",
                duration: 5000,
                close: true,
                gravity: "top",
                position: "right",
                stopOnFocus: true,
                style: {
                    background: "#fff",
                    color: "#222",
                    padding: "10px 20px",
                    borderRadius: "4px",
                    border: "1px solid red",
                },
            }).showToast();
        }
    });

    $(educationWrapper).on("click", ".remove-form-group", function (e) {
        e.preventDefault();
        $(this).closest(".form-replicate").remove();
        educationCounter--;
    });

    // Replicate Experience (similar to education)
    var experienceWrapper = $("#form-replicate-experience"); // Fields wrapper
    var addExperienceButton = $("#add-experience"); // Add button ID
    var experienceCounter = 1; // Initial text box count

    function addExperienceForm(x) {
        const html = `
            <div class="form-replicate position-relative" id="form-replicate-experience-${x}">
                <hr/>
                <a href="#" class="remove-form-group" data-id="${x}">
                    <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M6 5H18M9 5V5C10.5769 3.16026 13.4231 3.16026 15 5V5M9 20H15C16.1046 20 17 19.1046 17 18V9C17 8.44772 16.5523 8 16 8H8C7.44772 8 7 8.44772 7 9V18C7 19.1046 7.89543 20 9 20Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </a>
                <div class="row align-items-top">
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Industry Type</label>
                            <select name="industry_type[${x}]" class="form-select" required>
                                <option value="" hidden="" selected="">Select Your Preferred Industry</option>
                                <option value="Industry 1">Industry 1</option>
                                <option value="Industry 2">Industry 2</option>
                                <option value="Industry 3">Industry 3</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Designation</label>
                            <input type="text" name="designation[${x}]" class="form-control" placeholder="Enter your Designation" maxlength="100" required>
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Organization</label>
                            <input type="text" name="organization[${x}]" class="form-control" maxlength="100" placeholder="Enter your organization">
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Job start date</label>
                            <input type="date" name="job_tenure_from[${x}]" class="form-control" min="1980-03-15" max="2030-12-31" required>
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3">
                        <div>
                            <label class="form-label">Job end date</label>
                            <input type="date" name="job_tenure_to[${x}]" min="1980-03-15" max="2030-12-31" class="form-control">
                        </div>
                    </div>
                    <div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4 mb-3 align-self-end">
                        <label class="form-label">
                            <input type="checkbox" name="job_tenure_in_process[${x}]"> Currently working here
                        </label>
                    </div>
                </div>
            </div>
        `;

        $(experienceWrapper).append(html); // Append the dynamic HTML to the wrapper

        // Add validation rules for the new group
        addDynamicValidationRules("industry_type", x);
        addDynamicValidationRules("designation", x, {
            validateDesignation: true, // Custom rule for designation
             maxlength: 100,
            messages: {
                validateDesignation: "Please enter a valid designation (alphanumeric only).",
                maxlength: "Designation must be less than 100 characters."
            },
        });
        addDynamicValidationRules("organization", x, {
            validateOrganization: true, // Custom rule for designation
            maxlength: 100,
            messages: {
                validateOrganization: "Please enter a valid organization name (alphanumeric only).",
                maxlength: "organization name must be less than 100 characters.",
            },
        });
        addDynamicValidationRules("job_tenure_from", x);
    }

    $(addExperienceButton).click(function (e) {
        e.preventDefault();
        if (experienceCounter < max_fields) {
            experienceCounter++;
            addExperienceForm(experienceCounter);
        } else {
            Toastify({
                text: "Max 8 experiences allowed",
                duration: 5000,
                close: true,
                gravity: "top",
                position: "right",
                stopOnFocus: true,
                style: {
                    background: "#fff",
                    color: "#222",
                    padding: "10px 20px",
                    borderRadius: "4px",
                    border: "1px solid red",
                },
            }).showToast();
        }
    });

    $(experienceWrapper).on("click", ".remove-form-group", function (e) {
        e.preventDefault();
        $(this).closest(".form-replicate").remove();
        experienceCounter--;
    });
});