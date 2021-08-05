function predicttext() {
  if (!$("#inputText").val().trim().length) {
    event.preventDefault();
    event.stopPropagation();
    alert("Ingrese un parrafo");
    return false;
  } else {
    $.ajax({
      url: "/predic",
      type: "POST",
      data: JSON.stringify({ answer: $("#inputText").val() }),
      success: function (data) {
        resp = JSON.parse(data);
          console.log(resp);
        if (resp) {
          $("#similitudJC").attr("hidden", false).html(`
            <div class='container'>
            <table class="table">
            <thead>
              <th>#</th>
              <td>ENFOQUE PSICOSOCIAL - COMUNITARIO</td>
              <td>MODELO BIO MEDICO</td>
              <td>ENFOQUE COTIDIANO"</td>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Jaccard</th>
                <td>${resp.jacc_epc.toFixed(2)}</td>
                <td>${resp.jacc_mbm.toFixed(2)}</td>
                <td>${resp.jacc_ec.toFixed(2)}</td>
              </tr>
              <tr>
                <th scope="row">Coseno</th>
                <td>${resp.cos_epc.toFixed(2)}</td>
                <td>${resp.cos_mbm.toFixed(2)}</td>
                <td>${resp.cos_ec.toFixed(2)}</td>
              </tr>
            </tbody>
          </table>
            </div>
        `);

        }
      },
      error: function (err) {
        console.log(err);
      },
    });
  }
}
//   resp = JSON.parse(data);
// console.log(resp);
