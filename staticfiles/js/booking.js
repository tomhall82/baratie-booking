document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded'); // Log to confirm JS file is loaded
    
    const deleteModal = document.getElementById('deleteModal');
    const modalBookingName = document.getElementById('modalBookingName');
    const modalDeleteForm = document.getElementById('modalDeleteForm');

    deleteModal.addEventListener('show.bs.modal', function (event) {
        console.log('Modal about to be shown'); // Log to confirm modal event is firing

        const button = event.relatedTarget;
        const bookingName = button.getAttribute('data-name');
        const deleteUrl = button.getAttribute('data-url');

        console.log('Booking Name:', bookingName);
        console.log('Delete URL:', deleteUrl);

        modalBookingName.textContent = bookingName;
        modalDeleteForm.action = deleteUrl;
    });
});
