$.getJSON( "HSBC_2017-03-13.json", function( data ) {

	
	$.each(data["date"],function(index, datos){
		$.each(datos["indice"],function(ab,valor){
			console.log("valor");
		});
	});
}
