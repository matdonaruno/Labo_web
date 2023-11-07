
$(document).ready(function(){
  $.extend( $.fn.dataTable.defaults, {
    language: {
        url: "http://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Japanese.json"
    }
  }); 
  $('#POST').DataTable(
    {
      'paging':true,
      "dom": '<"dt-buttons"Bf><"clear">lirtp',
      "dom":"lBfrtip",
      "buttons": [
        'colvis',
        'copyHtml5',
        'csvHtml5',
        'excelHtml5',
        'pdfHtml5',
        'print'
      ],
      "order": [[ 0, "desc" ]],
      
      
  }
  );
});
