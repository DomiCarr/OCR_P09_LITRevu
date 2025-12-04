// -------------------------------------------------------------------
// File: ticket_preview.js
// Purpose: Display a preview of the selected ticket image
//          immediately after choosing a file, without submitting the form
// -------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
    // Get the hidden file input and the <img> used for preview
    const input = document.getElementById("id_image");
    const preview = document.getElementById("imagePreview");

    // If elements do not exist on the page, skip script
    if (!input || !preview) return;

    // Triggered each time the user selects a new file
    input.addEventListener("change", function () {
        const file = this.files[0];

        // No file selected -> hide preview and reset source
        if (!file) {
            preview.style.display = "none";
            preview.src = "";
            return;
        }

        // Use FileReader to load image locally without backend upload
        const reader = new FileReader();

        // When file is fully read, assign it to preview <img>
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = "block"; // show image
        };

        // Convert file to base64 for immediate preview
        reader.readAsDataURL(file);
    });
});
