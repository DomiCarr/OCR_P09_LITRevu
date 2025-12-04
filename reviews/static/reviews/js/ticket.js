// ticket.js
// Handles create/edit modes and image preview.

document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const mode = params.get('action') || 'create';
    const ticketId = params.get('id') || null;

    document.getElementById('mode').value = mode;
    document.getElementById('ticket_id').value = ticketId;

    const btnCreate = document.getElementById('btn_create');
    const btnSave = document.getElementById('btn_save');
    const btnDelete = document.getElementById('btn_delete');

    // Switch UI depending on mode
    if (mode === 'edit') {
        btnCreate.style.display = 'none';
        btnSave.style.display = 'inline-block';
        btnDelete.style.display = 'inline-block';

        loadTicket(ticketId);
    } else {
        btnCreate.style.display = 'inline-block';
        btnSave.style.display = 'none';
        btnDelete.style.display = 'none';
    }

    // Image preview setup
    const inputImage = document.getElementById("id_image");
    const preview = document.getElementById("imagePreview");

    inputImage.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            preview.src = URL.createObjectURL(file);
            preview.style.display = "block";
        } else {
            preview.style.display = "none";
        }
    });
});

// Loads data for edit mode (placeholder, replace with backend API)
function loadTicket(id) {
    const title = document.getElementById('title');
    const desc = document.getElementById('description');

    title.value = 'Sample title';
    desc.value = 'Sample description';
}

// Called when user creates a ticket
function createTicket() {
    console.log('Creating ticket...');
    document.getElementById('ticketForm').submit();
}

// Saves edited ticket
function saveTicket() {
    const id = document.getElementById('ticket_id').value;
    console.log('Saving ticket', id);
    document.getElementById('ticketForm').submit();
}

// Deletes edited ticket
function deleteTicket() {
    const id = document.getElementById('ticket_id').value;
    console.log('Deleting ticket', id);
    // Optionally: confirm before delete
}
