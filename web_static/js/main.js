document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById('toggleFilters');
    const filtersSection = docuemnt.getElementById('filtersSection');

    toggleButton.addEventListener('click', function () {
        filtersSection.classList.toggle('active');
    });
});