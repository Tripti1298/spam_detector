// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const submitButton = document.querySelector('button[type="submit"]');

    // Add an event listener to the form's submit event
    form.addEventListener('submit', function(event) {
        // Show a message or disable the button to indicate processing
        submitButton.innerHTML = 'Processing...';
        submitButton.disabled = true;
    });
});