document.querySelectorAll('.charge-filters').forEach(form => {
    form.querySelectorAll('input[type="radio"], select').forEach(input => {
        input.addEventListener('change', () => form.requestSubmit());
    });
});
