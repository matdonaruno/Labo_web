$(document).ready(function() {

	$('#POST').DataTable(
		{
			"buttons": [
				'colvis',
				'copyHtml5',
        'csvHtml5',
				'excelHtml5',
        'pdfHtml5',
				'print'
			],
			"columnDefs": [
				{ "orderable": false},
				{ "width": "20%", "targets": 0 }
			],
      "order": [[ 0, "desc" ]],
			"dom": '<"dt-buttons"Bf><"clear">lirtp',
			"paging": false,
			"autoWidth": false,
			"scrollx": false,
			"stateSave": true,
			"lengthChanged": false,
			"responsive": true,
		}
	);
	})
	$(".btn-print").click(function () {
		window.print();
	});