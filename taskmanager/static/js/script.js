
  document.addEventListener('DOMContentLoaded', function() {
    // side nav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(sidenav);

    //date picker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "Select"}

    });

    // select initialization

    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });