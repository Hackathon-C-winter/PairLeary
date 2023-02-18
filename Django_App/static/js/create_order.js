flatpickr.defaultConfig = {
    locale: 'ja',
    dateFormat: 'Y-m-d'
}
flatpickr('#calender', {
    altInput: true,
    altFormat: 'Y年n月j日',
    dateFormat: 'Y-m-d',
    minDate: 'today'
});
