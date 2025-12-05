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

    // Initial check
    checkFields();

    // Sur modification des champs texte
    titleInput.addEventListener("input", checkFields);
    descInput.addEventListener("input", checkFields);

    // Sur sélection d’une image
    inputImage.addEventListener("change", () => {
        const file = inputImage.files[0];
        if (file) {
            // Affiche la preview
            preview.src = URL.createObjectURL(file);
            preview.style.display = "block";
        } else {
            // Pas de fichier => cache
            preview.src = "";
            preview.style.display = "none";
        }
        checkFields();
    });
});
