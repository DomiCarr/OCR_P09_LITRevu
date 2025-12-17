// reviews/static/reviews/js/ticket.js
document.addEventListener('DOMContentLoaded', () => {
    const titleInput = document.getElementById("title");
    const descInput = document.getElementById("description");
    const inputImage = document.getElementById("image");
    const preview = document.getElementById("imagePreview");
    const submitBtn = document.getElementById("submitBtn");

    function checkFields() {
        const okTitle = titleInput.value.trim().length > 0;
        const okDesc = descInput.value.trim().length > 0;
        const okImg = preview.src && preview.src.trim() !== "";
        submitBtn.disabled = !(okTitle && okDesc && okImg);
    }

    // Initial alt update if editing
    if (preview.src && preview.src.trim() !== "") {
        preview.alt = titleInput.value || "Ticket image";
    }

    // Initial check
    checkFields();

    // On title change
    titleInput.addEventListener("input", () => {
        preview.alt = titleInput.value || "Ticket image"; // Update alt dynamically
        checkFields();
    });

    // On description change
    descInput.addEventListener("input", checkFields);

    // On image selection
    inputImage.addEventListener("change", () => {
        const file = inputImage.files[0];
        if (file) {
            preview.src = URL.createObjectURL(file);
            preview.style.display = "block";
            preview.alt = titleInput.value || "Ticket image";
        } else {
            preview.src = "";
            preview.style.display = "none";
            preview.alt = "";
        }
        checkFields();
    });
});
