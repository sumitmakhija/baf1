(function($) {
    $(document).ready(function() {
        // Handle gallery button click
        $(document).on('click', '.gallery-button', function() {
            const fieldName = $(this).data('field-name');
            const galleryUrl = $(this).data('gallery-url');
            
            // Open a popup window with the gallery
            const popup = window.open(galleryUrl + '?field_name=' + fieldName, 'blobImageGallery', 
                'width=900,height=600,resizable=yes,scrollbars=yes');
            
            // Focus on the popup
            popup.focus();
        });
        
        // This function will be called from the popup window when an image is selected
        window.setSelectedImage = function(fieldName, imageUrl) {
            // Find the hidden input field for the selected image
            const hiddenInput = $('input[name="' + fieldName + '_blob_url"]');
            
            // If it doesn't exist, create it
            if (hiddenInput.length === 0) {
                const input = $('<input>').attr({
                    type: 'hidden',
                    name: fieldName + '_blob_url',
                    value: imageUrl
                });
                $('.blob-image-picker').append(input);
            } else {
                // Otherwise, update its value
                hiddenInput.val(imageUrl);
            }
            
            // Update the preview image if it exists
            const previewContainer = $('input[name="' + fieldName + '"]').closest('.blob-image-picker').find('.current-image');
            if (previewContainer.length) {
                previewContainer.html('<img src="' + imageUrl + '" alt="Selected image" style="max-width: 200px; max-height: 200px; margin-top: 10px;">');
            } else {
                // Create a preview container if it doesn't exist
                const newPreview = $('<div class="current-image"><img src="' + imageUrl + '" alt="Selected image" style="max-width: 200px; max-height: 200px; margin-top: 10px;"></div>');
                $('input[name="' + fieldName + '"]').closest('.blob-image-picker').append(newPreview);
            }
        };
    });
})(django.jQuery);
