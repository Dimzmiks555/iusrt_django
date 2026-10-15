document.querySelectorAll('.file-picker input[type="file"]').forEach(input => {
    input.addEventListener('change', () => {
        const name = input.closest('.file-picker').querySelector('.file-picker-name');
        name.textContent = input.files.length ? input.files[0].name : 'Чек или платёжное поручение';
    });
});
