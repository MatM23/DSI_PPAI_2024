function importarActVinosBodega() {
   let tablaBodegas = document.getElementById('tabla-bodegas');
   tablaBodegas.innerHTML = ''; // Limpiar la lista

   fetch("http://127.0.0.1:5000/api/bodega/actualizables")
   .then(respuesta => respuesta.json())
   .then(bodegas => {
      console.log(bodegas)
       bodegas.forEach(bodega => {
           const row = `
               <tr>
                   <td><input class="form-check-input" type="radio" name="opcion" id="seleccionBodega" style="position: center"></td>
                   <td>${bodega}</td>
               </tr>
               `
           tablaBodegas.innerHTML += row;
       });

       // Mostrar el botón al seleccionar un radio
       const radios = document.querySelectorAll('input[name="opcion"]');
       const actualizarBodegaBtn = document.getElementById('actualizarBodega');
       radios.forEach(radio => {
           radio.addEventListener('change', function() {
               actualizarBodegaBtn.style.display = 'inline-block';
           });
       });
   })
   .catch(error => {
       console.error('Error:', error);
   });
}