$(document).ready(function() {
	//Only needed for the filename of export files.
	//Normally set in the title tag of your page.
	document.title='Simple DataTable';
	// DataTable initialisation
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
			
      "order": [[ 0, "desc" ]],
			"dom": '<"dt-buttons"Bf><"clear">lirtp',
			"paging": true,
			"autoWidth": false,
			"columnDefs": [
				{ "orderable": false},
				{ "targets": [0,1,2,3,4], "width": "5%" }
			],
			
			"order": [ [ 3, "desc"] ],
			"scrollx": true,
			"stateSave": true,
			"lengthChanged": true,
		}
	);
	
			//REMOVE EDIT AND DELETE EVENTS FROM ALL BUTTONS
			$('.dt-edit').off('click');
			$('.dt-delete').off('click');
	})